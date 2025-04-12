import pytest
import logging
import os

# Настройка логирования
log_dir = r""#нужно вставить путь до своего местоположения файла
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, 'test_onboarding_get_started.log')

# Создаем логгер
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Создаем обработчик для записи в файл
file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
file_handler.setLevel(logging.INFO)

# Создаем форматтер
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)

@pytest.mark.usefixtures("onboarding")
def test_get_started_button(onboarding, device_logs):
    """Тестирование кнопки 'Get Started' на последнем экране онбординга"""

    logger.info("Начало теста кнопки 'Get Started' на последнем экране онбординга")
    test_passed = True

    # Пропускаем первые 3 экрана
    for i in range(3):
        logger.info(f"Экран {i + 1}: Проверка видимости кнопки 'Continue'")
        if not onboarding.is_continue_button_visible():
            logger.error(f"Кнопка 'Continue' не отображается на экране {i + 1}")
            test_passed = False
            break  # Если кнопка "Continue" не отображается, нет смысла продолжать
        else:
            logger.info(f"Кнопка 'Continue' отображается на экране {i + 1}")

        logger.info(f"Экран {i + 1}: Нажатие на кнопку 'Continue'")
        onboarding.tap_continue()

    # Проверка кнопки 'Get Started'
    if test_passed:  # Продолжаем, только если предыдущие шаги прошли успешно
        logger.info("Проверка видимости кнопки 'Get Started'")
        if not onboarding.is_get_started_visible():
            logger.error("Кнопка 'Get Started' не отображается")
            test_passed = False
        else:
            logger.info("Кнопка 'Get Started' отображается")

        logger.info("Нажатие на кнопку 'Get Started'")
        onboarding.tap_get_started()

        logger.info("Проверка видимости главного экрана")
        if not onboarding.is_main_screen_visible():
            logger.error("Главный экран не отображается после нажатия 'Get Started'")
            test_passed = False
        else:
            logger.info("Главный экран отображается после нажатия 'Get Started'")

    if test_passed:
        logger.info("Тест успешно завершен")
    else:
        logger.error("Тест завершился с ошибками")

    assert test_passed, "Тест завершился с ошибками (см. логи)"