import subprocess
import signal
import os
import pytest
import platform
from drivers.appium_driver import create_driver
from pages.functional_tests_page.onboarding_pages.onboarding_page import OnboardingPage

@pytest.fixture
def driver():
    d = create_driver()
    yield d
    d.quit()

@pytest.fixture
def onboarding(driver):
    return OnboardingPage(driver)

def run_adb_logcat(log_file, tag="wikipedia.alpha"):
    """Запускает adb logcat и записывает логи в файл."""
    try:
        kwargs = {
            'stdout': open(log_file, 'w', encoding='utf-8'),
            'stderr': subprocess.STDOUT
        }
        # Добавляем preexec_fn только на Unix-системах
        if platform.system() != "Windows":
            kwargs['preexec_fn'] = os.setsid

        process = subprocess.Popen(['adb', 'logcat', f'{tag}:I', '*:S'],
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
def device_logs():
    """Запускает и останавливает логирование ADB перед и после теста."""
    log_file = r"" #нужно вставить путь до своего местоположения файла
    tag = "wikipedia.alpha"

    # Создаем директорию, если ее нет
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    process = run_adb_logcat(log_file, tag)

    if process:
        print(f"Запись логов в {log_file} началась.")
        yield # Предоставляем управление тесту
        print("Запись логов завершена.")
        stop_process(process)
        print(f"Логи сохранены в {log_file}")
    else:
        print("Не удалось запустить adb logcat.")
        yield # Все равно передаем управление тесту, но без логирования