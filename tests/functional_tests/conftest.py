import logging
import os
import platform
import signal
import subprocess
from typing import Generator

import allure
import pytest
import requests
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.webdriver import WebDriver as Remote
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from config.settings import Config
from drivers.appium_driver import create_driver
from pages.functional_tests_page.all_pages import AllPages
from utils.logger_utils import setup_logger, setup_logger_device, setup_service_logger

ADB_TAG = "wikipedia.alpha"

# Константы путей
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_ALLURE_DIR = os.path.join(_PROJECT_ROOT, "allure")

@pytest.fixture(scope="session", autouse=True)
def appium_service(request):
    worker_id = getattr(request.config, "workerinput", {}).get("workerid", "master")
    device_config = Config.get_device_config(worker_id)
    port = device_config["appiumPort"]

    """Запуск Appium сервера"""
    # Создаём логгер отдельный для Appium
    logs_root_dir = os.path.join(_PROJECT_ROOT, "logs", "session")
    os.makedirs(logs_root_dir, exist_ok=True)
    log_file = os.path.join(logs_root_dir, f"appium_service_{port}.log")

    # Настраиваем логгер
    logger = logging.getLogger(f"appium_service_{worker_id}")
    logger.setLevel(logging.DEBUG)
    if logger.hasHandlers():
        logger.handlers.clear()

    file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info(f"🚀 Запуск Appium сервера на порту {port}...")

    service = AppiumService()
    service.start(
        args=[
            '--port', str(port),
            '--log-level', 'error',
            '--allow-insecure', 'parallel_sessions',
            '--relaxed-security'
        ],
        timeout_ms=20000
    )

    if not (service.is_running and service.is_listening):
        logger.error("❌ Appium сервер не запустился")
        raise RuntimeError("Appium сервер не запустился")

    logger.info("✅ Appium сервер успешно запущен")

    yield

    logger.info("🛑 Остановка Appium сервера...")
    service.stop()
    logger.info("✅ Appium сервер остановлен")

def _get_worker_logger(worker_id: str, name: str, clear: bool = True) -> logging.Logger:
    """Создает и настраивает логгер для конкретного воркера"""
    LOGS_DIR = os.path.join(_PROJECT_ROOT, "logs", "driver")
    os.makedirs(LOGS_DIR, exist_ok=True)

    logger = logging.getLogger(f"{name}_{worker_id}")
    logger.setLevel(logging.DEBUG)

    # Очистка предыдущих обработчиков
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)

    # Настройка файлового обработчика
    # Очистка или дозапись в лог
    log_file = os.path.join(LOGS_DIR, f"{name}_{worker_id}.log")
    file_mode = 'w' if clear else 'a'

    handler = logging.FileHandler(log_file, mode=file_mode, encoding='utf-8')
    handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))
    logger.addHandler(handler)

    return logger

def _wait_for_appium_ready(port: int, timeout: float = 5.0, interval: float = 1.0) -> bool:
    url = f"http://localhost:{port}/status"
    session = requests.Session()
    adapter = HTTPAdapter(
        max_retries=Retry(
            total=int(timeout / interval),
            backoff_factor=interval,
            status_forcelist=[500, 502, 503, 504]
        )
    )
    session.mount("http://", adapter)

    try:
        response = session.get(url, timeout=interval)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

@pytest.fixture(scope="function")
def driver(request) -> Generator[Remote, None, None]:
    """Фикстура для создания и закрытия драйвера с улучшенным логированием"""
    worker_id = getattr(request.config, "workerinput", {}).get("workerid", "master")
    logger = _get_worker_logger(worker_id, "driver")
    port = Config.get_device_config(worker_id)["appiumPort"]

    # Ожидаем готовности Appium сервера
    logger.debug("⏳ Ожидание готовности Appium сервера...")
    if not _wait_for_appium_ready(port):
        logger.error("❌ Appium сервер не доступен")
        pytest.fail("Appium сервер не запущен или не отвечает")

    driver_instance = None
    try:
        logger.debug("🚀 Инициализация драйвера...")
        driver_instance = create_driver(worker_id)
        logger.info("✅ Драйвер успешно создан")
        yield driver_instance
    except Exception as e:
        logger.error(f"❌ Ошибка при создании драйвера: {str(e)}")
        pytest.fail(f"Не удалось инициализировать драйвер: {str(e)}")
    finally:
        if driver_instance:
            try:
                logger.debug("🛑 Завершение работы драйвера...")
                driver_instance.quit()
                logger.info("✅ Драйвер успешно закрыт")
            except Exception as e:
                logger.error(f"⚠️ Ошибка при закрытии драйвера: {str(e)}")

def pytest_sessionstart(session):
    """Очищает лог-файлы только один раз в начале сессии"""
    LOGS_DIR = os.path.join(_PROJECT_ROOT, "logs", "driver")
    os.makedirs(LOGS_DIR, exist_ok=True)

    for filename in os.listdir(LOGS_DIR):
        file_path = os.path.join(LOGS_DIR, filename)
        if filename.endswith(".log"):
            with open(file_path, "w", encoding="utf-8"):
                pass  # очищает файл

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    """Хук для логирования информации о запуске теста"""
    worker_id = getattr(item.config, "workerinput", {}).get("workerid", "master")
    logger = _get_worker_logger(worker_id, "test_setup", clear=False)
    logger.debug(f"🔧 Тест '{item.nodeid}' запускается на воркере {worker_id}")

@pytest.fixture(scope="function")
def pages(driver, logger):
    return AllPages(driver, logger)

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

@pytest.fixture(scope="function")
def service_logger(request):
    """Логгер инфраструктурного уровня — для фикстур вроде device_logs и appium_service"""
    test_name = request.node.name
    test_file_path = request.fspath
    project_root = str(request.config.rootdir)

    test_module_dir = os.path.basename(os.path.dirname(test_file_path))
    log_dir_path = os.path.join(project_root, "logs", f"{test_module_dir}_logs")
    os.makedirs(log_dir_path, exist_ok=True)

    return setup_service_logger(test_name, log_dir_path)

@pytest.fixture(scope="function", autouse=True)
def device_logs(request, service_logger):
    test_name = request.node.name
    test_file_path = request.fspath
    project_root = str(request.config.rootdir)

    # Получаем worker_id и udid
    worker_id = getattr(request.config, "workerinput", {}).get("workerid", "master")
    device_config = Config.get_device_config(worker_id)
    udid = device_config["udid"]

    # Путь к логам
    test_module_dir = os.path.basename(os.path.dirname(test_file_path))
    log_dir_path = os.path.join(project_root, "logs", f"{test_module_dir}_logs")
    os.makedirs(log_dir_path, exist_ok=True)

    log_file = setup_logger_device(test_name, log_dir_path)

    try:
        subprocess.run(['adb', '-s', udid, 'logcat', '-c'], check=True)
        subprocess.run(['adb', '-s', udid, 'logcat', '-G', '2M'], check=True)
        service_logger.info(f"✅ logcat очищен и буфер увеличен для {udid}")
    except subprocess.CalledProcessError as e:
        service_logger.error(f"❌ Ошибка при очистке logcat или установке буфера: {e}")
        yield
        return
    except FileNotFoundError:
        service_logger.error("❌ adb не найден в PATH")
        yield
        return

    try:
        kwargs = {
            'stdout': open(log_file, 'w', encoding='utf-8'),
            'stderr': subprocess.STDOUT
        }
        if platform.system() != "Windows":
            kwargs['preexec_fn'] = os.setsid

        process = subprocess.Popen(['adb', '-s', udid, 'logcat', f'{ADB_TAG}:I', '*:S'], **kwargs)
        service_logger.info(f"🔍 Логирование устройства {udid} начато: {log_file}")
    except Exception as e:
        service_logger.error(f"❌ Не удалось запустить adb logcat: {e}")
        yield
        return

    yield

    try:
        if platform.system() == "Windows":
            subprocess.run(['taskkill', '/F', '/T', '/PID', str(process.pid)], check=True)
        else:
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        process.wait()
        service_logger.info(f"✅ Логирование завершено. Лог сохранён в {log_file}")
        try:
            with open(log_file, 'r', encoding='utf-8') as f:
                log_content = f.read()
                allure.attach(
                    name="Логи устройства (logcat)",
                    body=log_content,
                    attachment_type=allure.attachment_type.TEXT
                )
        except Exception as e:
            service_logger.error(f"❌ Не удалось прикрепить логи к Allure: {e}")

    except Exception as e:
        service_logger.error(f"❌ Ошибка при остановке logcat процесса: {e}")

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

@pytest.fixture(scope="function")
def skip_onboarding(pages, logger):
    """Пропускает экраны онбординга, если они появляются"""
    saved = pages.saved

    with allure.step("⏭️ Пропуск онбординга"):
        try:
            for i in range(3):
                if saved.clicks.safe_click(saved.CONTINUE_BTN):
                    logger.debug(f"Пропущен экран онбординга {i + 1}")
                else:
                    break

            if saved.clicks.safe_click(saved.GET_STARTED_BTN):
                logger.info("Онбординг успешно пропущен")
            else:
                logger.debug("Экран онбординга не обнаружен")

        except Exception as e:
            logger.warning(f"Ошибка при пропуске онбординга: {str(e)}")
            allure.attach(
                name="Ошибка пропуска онбординга",
                body=str(e),
                attachment_type=allure.attachment_type.TEXT
            )

    return pages

@pytest.fixture(scope="function")
def log_in(logger, skip_onboarding):
    """Выполняет вход в аккаунт с обработкой разрешений"""
    saved = skip_onboarding.saved

    try:
        with allure.step(f"Авторизация пользователя"):
            with allure.step("Переход в раздел 'Saved'"):
                saved.clicks.safe_click(saved.SAVED_BTN)

            with allure.step("Открытие экрана авторизации"):
                saved.clicks.safe_click(saved.POSITIVE_BTN)
                saved.clicks.safe_click(saved.CREATE_ACCOUNT_LOGIN_BUTTON_BTN)

            with allure.step("Ввод учетных данных"):
                assert saved.log_in_to_account(), "Не удалось ввести логин/пароль"
                saved.clicks.safe_click(saved.LOGIN_BUTTON_BTN)

            with allure.step("Нажатие кнопки 'Dont allow'"):
                logger.debug("Ищем кнопку 'Dont allow'")
                assert saved.clicks.safe_click(saved.PERMISSION_DENY_BUTTON_BTN), "Кнопка 'Dont allow' не найдена"
                logger.info("Кнопка 'Dont allow' найдена и нажата")

            logger.info("Успешная авторизация")
            yield saved

    except Exception as e:
        logger.error(f"Ошибка авторизации: {str(e)}")
        allure.attach(
            name="Ошибка авторизации",
            body=str(e),
            attachment_type=allure.attachment_type.TEXT
        )
        pytest.fail(f"Тест прерван - не удалось выполнить вход: {str(e)}")

@pytest.fixture(scope="function")
def log_out(request, logger, pages):
    """Выполняет выход из аккаунта"""
    def fin():
        saved = pages.saved

        try:
            with allure.step("🚪 Выход из аккаунта"):
                assert saved.clicks.safe_click(saved.MORE_BTN), "❌ Нет кнопки 'More'"
                assert saved.clicks.safe_click(saved.SETTINGS_TV), "❌ Нет кнопки 'Settings'"

                # Прокручиваем до появления кнопки Log out
                MAX_SWIPE_ATTEMPTS = 10
                for _ in range(MAX_SWIPE_ATTEMPTS):
                    try:
                        if saved.clicks.is_visible(saved.LOGOUT_BUTTON_BTN):
                            break
                    except:
                        pass
                    saved.swipes.swipe_up()
                else:
                    raise AssertionError("❌ Кнопка 'Log out' не найдена после прокрутки")

                assert saved.clicks.safe_click(saved.LOGOUT_BUTTON_BTN), "❌ Нет кнопки 'Log out'"
                assert saved.clicks.safe_click(saved.BUTTON1_BTN), "❌ Подтверждение 'Log out' не найдено"

                assert saved.clicks.is_visible(saved.SAVED_BTN), "❌ Не вышли из аккаунта"
                logger.info("✅ Аккаунт успешно разлогинен")

        except Exception as e:
            logger.error(f"Ошибка при выходе: {str(e)}")
            allure.attach(
                name="Ошибка выхода",
                body=str(e),
                attachment_type=allure.attachment_type.TEXT
            )
            raise

    request.addfinalizer(fin)