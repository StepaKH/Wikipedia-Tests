import subprocess
import signal
import pytest
import allure
import platform
import os
import shutil
from appium.webdriver.appium_service import AppiumService
from drivers.appium_driver import create_driver
from pages.functional_tests_page.onboarding_pages.onboarding_page import OnboardingPage
from utils.logger_utils import setup_logger, setup_logger_device

ADB_TAG = "wikipedia.alpha"

# Константы путей
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_ALLURE_DIR = os.path.join(_PROJECT_ROOT, "allure")

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
    test_file_path = request.fspath

    # Получаем корень проекта через pytest
    project_root = str(request.config.rootdir)

    # Путь к общей папке logs в корне проекта
    logs_root_dir = os.path.join(project_root, "logs")
    os.makedirs(logs_root_dir, exist_ok=True)

    # Извлекаем имя директории, где лежит тест
    test_module_dir = os.path.basename(os.path.dirname(test_file_path))

    # Создаём директорию для логов: <корень>/logs/<module>_logs
    log_dir_name = f"{test_module_dir}_logs"
    log_dir_path = os.path.join(project_root, "logs", log_dir_name)
    os.makedirs(log_dir_path, exist_ok=True)

    logger = setup_logger(test_name, log_dir_path)
    logger.info(f"🚀 Starting test: {test_name}")

    yield logger

    logger.info(f"✅ Test finished: {test_name}")

@pytest.fixture(scope="function", autouse=True)
def device_logs(request):
    """Автоматический запуск/остановка adb logcat перед каждым тестом с очисткой и увеличением буфера"""
    test_name = request.node.name
    test_file_path = request.fspath
    project_root = str(request.config.rootdir)

    # Путь к логам
    test_module_dir = os.path.basename(os.path.dirname(test_file_path))
    log_dir_path = os.path.join(project_root, "logs", f"{test_module_dir}_logs")
    os.makedirs(log_dir_path, exist_ok=True)

    # Подготовка файла лога
    log_file = setup_logger_device(test_name, log_dir_path)

    # Очистка логов и настройка буфера
    try:
        subprocess.run(['adb', 'logcat', '-c'], check=True)
        subprocess.run(['adb', 'logcat', '-G', '2M'], check=True)
        print("✅ logcat очищен и буфер увеличен")
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка при очистке logcat или установке буфера: {e}")
    except FileNotFoundError:
        print("❌ adb не найден в PATH")
        yield
        return

    # Запуск логирования
    try:
        kwargs = {
            'stdout': open(log_file, 'w', encoding='utf-8'),
            'stderr': subprocess.STDOUT
        }
        if platform.system() != "Windows":
            kwargs['preexec_fn'] = os.setsid

        process = subprocess.Popen(['adb', 'logcat', f'{ADB_TAG}:I', '*:S'], **kwargs)
        print(f"[{test_name}] 🔍 Логирование девайса начато: {log_file}")
    except Exception as e:
        print(f"[{test_name}] ❌ Не удалось запустить adb logcat: {e}")
        yield
        return

    yield  # Тест выполняется

    # Остановка процесса
    try:
        if platform.system() == "Windows":
            subprocess.run(['taskkill', '/F', '/T', '/PID', str(process.pid)], check=True)
        else:
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        process.wait()
        print(f"[{test_name}] ✅ Логирование завершено. Лог сохранён в {log_file}")
    except Exception as e:
        print(f"[{test_name}] ❌ Ошибка при остановке logcat процесса: {e}")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == 'call' and rep.failed:
        try:
            driver = item.funcargs['driver']
            # Сохраняем скриншот в директорию allure
            screenshot_dir = _ALLURE_DIR
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
    config.option.allure_report_dir = _ALLURE_DIR