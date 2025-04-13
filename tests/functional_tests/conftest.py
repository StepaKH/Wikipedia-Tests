import subprocess
import signal
import pytest
import platform
import time
import socket
from drivers.appium_driver import create_driver
from pages.functional_tests_page.onboarding_pages.onboarding_page import OnboardingPage
from utils.logger_utils import *

ADB_TAG = "wikipedia.alpha"

@pytest.fixture(scope="session", autouse=True)
def appium_service():
    """Автоматический запуск и остановка Appium сервера"""
    print("🚀 Запуск Appium сервера...")

    command = ["appium", "--log-level", "error"]

    if platform.system() != "Windows":
        process = subprocess.Popen(command, preexec_fn=os.setsid)
    else:
        process = subprocess.Popen(command, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)

    # Прямо внутри фикстуры: ожидание запуска Appium
    start_time = time.time()
    timeout = 15
    while time.time() - start_time < timeout:
        try:
            with socket.create_connection(("127.0.0.1", 4723), timeout=2):
                print("✅ Appium сервер успешно запущен")
                break
        except (OSError, ConnectionRefusedError):
            time.sleep(1)
    else:
        print("❌ Appium сервер не запустился за 15 секунд")
        process.terminate()
        raise RuntimeError("Appium сервер не запустился")

    yield  # Здесь запускаются тесты

    print("🛑 Остановка Appium сервера...")
    try:
        if platform.system() != "Windows":
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        else:
            subprocess.call(['taskkill', '/F', '/T', '/PID', str(process.pid)])
        print("✅ Appium сервер остановлен.")
    except Exception as e:
        print(f"❌ Ошибка при остановке Appium: {e}")

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
    test_name = request.node.name
    test_file_dir = os.path.dirname(request.fspath)

    log_dir = find_log_dir(test_file_dir)
    if log_dir is None:
        # Если директория не найдена, создадим дефолтную
        log_dir = os.path.join(test_file_dir, "default_log")
        os.makedirs(log_dir, exist_ok=True)

    return setup_logger(test_name, log_dir)

def run_adb_logcat(log_file):
    """Запускает adb logcat и записывает логи в файл."""
    try:
        kwargs = {
            'stdout': open(log_file, 'w', encoding='utf-8'),
            'stderr': subprocess.STDOUT
        }
        # Добавляем preexec_fn только на Unix-системах
        if platform.system() != "Windows":
            kwargs['preexec_fn'] = os.setsid

        process = subprocess.Popen(['adb', 'logcat', f'{ADB_TAG}:I', '*:S'],
                                   **kwargs)
        return process
    except FileNotFoundError:
        print("Ошибка: adb не найден в PATH.")
        return None

def stop_process(process):
    """Останавливает процесс."""
    if process:
        try:
            # Используем разные способы остановки процесса в зависимости от ОС
            if platform.system() == "Windows":
                subprocess.Popen(['taskkill', '/F', '/T', '/PID', str(process.pid)])
            else:
                os.killpg(os.getpgid(process.pid), signal.SIGTERM)
            process.wait()
            print("Процесс остановлен.")
        except ProcessLookupError:
            print("Процесс уже завершен.")

@pytest.fixture(scope="function")
def device_logs(request):
    """Запускает и останавливает логирование ADB перед и после теста."""
    test_name = request.node.name
    test_file_dir = os.path.dirname(request.fspath)

    log_dir = find_log_dir(test_file_dir)
    if log_dir is None:
        log_dir = os.path.join(test_file_dir, "default_log")
        os.makedirs(log_dir, exist_ok=True)

    log_file = setup_logger_device(test_name, log_dir)

    process = run_adb_logcat(log_file)
    if process:
        print(f"[{test_name}] Логирование в {log_file} началось.")
        yield
        stop_process(process)
        print(f"[{test_name}] Логирование завершено. Лог сохранен в {log_file}")
    else:
        print(f"[{test_name}] Не удалось запустить adb logcat.")
        yield