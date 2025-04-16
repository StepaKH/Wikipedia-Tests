import subprocess
import signal
import pytest
import allure
import platform
import logging
import os
from appium.webdriver.appium_service import AppiumService
from drivers.appium_driver import create_driver
from pages.functional_tests_page.onboarding_pages.onboarding_page import OnboardingPage
from utils.logger_utils import setup_logger, setup_logger_device, get_logger

ADB_TAG = "wikipedia.alpha"

# Константы путей
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOGS_DIR = os.path.join(PROJECT_ROOT, "logs", "onboarding_logs")
ALLURE_DIR = os.path.join(PROJECT_ROOT, "allure", "onboarding_allure")


@pytest.fixture(scope="session", autouse=True)
def appium_service():
    """Запуск Appium сервера"""
    service = AppiumService()
    print("🚀 Запуск Appium сервера...")
    service.start(args=['--log-level', 'error'], timeout_ms=15000)

    if not (service.is_running and service.is_listening):
        raise RuntimeError("❌ Appium сервер не запустился")

    yield
    print("🛑 Остановка Appium сервера...")
    service.stop()


@pytest.fixture(scope="function")
def driver():
    d = create_driver()
    yield d
    d.quit()


@pytest.fixture(scope="function")
def onboarding(driver):
    return OnboardingPage(driver)


@pytest.fixture(scope="function")
def logger(request):
    """Фикстура логгера для каждого теста с перезаписью файлов"""
    test_name = request.node.name
    os.makedirs(LOGS_DIR, exist_ok=True)

    # Удаляем старый лог-файл если существует
    log_file = os.path.join(LOGS_DIR, f"{test_name}.log")
    if os.path.exists(log_file):
        os.remove(log_file)

    logger = setup_logger(test_name, PROJECT_ROOT)
    logger.info(f"🚀 Starting test: {test_name}")

    yield logger

    logger.info(f"✅ Test finished: {test_name}")
    for handler in logger.handlers:
        handler.close()
    logging.shutdown()


@pytest.fixture(scope="function", autouse=True)
def device_logs(request, logger):
    """Фикстура для логирования устройств с перезаписью"""
    test_name = request.node.name
    os.makedirs(LOGS_DIR, exist_ok=True)

    # Удаляем старый лог устройства если существует
    log_file = os.path.join(LOGS_DIR, f"{test_name}_device.log")
    if os.path.exists(log_file):
        os.remove(log_file)

    # Очистка логов и настройка буфера
    try:
        subprocess.run(['adb', 'logcat', '-c'], check=True)
        subprocess.run(['adb', 'logcat', '-G', '2M'], check=True)
        logger.info("logcat очищен и буфер увеличен")
    except subprocess.CalledProcessError as e:
        logger.error(f"Ошибка при очистке logcat: {e}")
    except FileNotFoundError:
        logger.error("adb не найден в PATH")
        yield
        return

    # Запуск логирования
    try:
        kwargs = {
            'stdout': open(log_file, 'w', encoding='utf-8'),
            'stderr': subprocess.STDOUT,
            'creationflags': subprocess.CREATE_NEW_PROCESS_GROUP if platform.system() == "Windows" else 0
        }
        process = subprocess.Popen(['adb', 'logcat', f'{ADB_TAG}:I', '*:S'], **kwargs)
        logger.info(f"Логирование девайса начато: {log_file}")
    except Exception as e:
        logger.error(f"Не удалось запустить adb logcat: {e}")
        yield
        return

    yield

    # Остановка процесса
    try:
        if platform.system() == "Windows":
            subprocess.run(['taskkill', '/F', '/T', '/PID', str(process.pid)], check=True)
        else:
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        logger.info(f"Логирование завершено. Лог сохранён в {log_file}")
    except Exception as e:
        logger.error(f"Ошибка при остановке logcat: {e}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == 'call' and rep.failed:
        try:
            driver = item.funcargs['driver']
            # Сохраняем скриншот в директорию allure
            screenshot_dir = os.path.join(str(item.config.rootdir), "allure", "onboarding_allure")
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{item.nodeid.replace('::', '_')}.png")
            driver.save_screenshot(screenshot_path)

            # Прикрепляем к allure отчету
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            item.funcargs['logger'].error(f"Failed to take screenshot: {str(e)}")

def pytest_configure(config):
    """Конфигурация pytest для сохранения Allure-отчетов"""
    config.option.allure_report_dir = ALLURE_DIR
