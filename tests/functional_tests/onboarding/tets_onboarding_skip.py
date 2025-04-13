import pytest
import logging
import os

# Настройка логирования
log_dir = r""#нужно вставить путь до своего местоположения файла
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, 'test_onboarding_skip.log')

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

@pytest.mark.parametrize("screen_count", [0, 1, 2])
def test_skip_button_on_screens(onboarding, screen_count, device_logs):
    """Проверка кнопки 'Skip' на 1, 2 и 3 экранах онбординга"""

    logger.info(f"Начало теста кнопки 'Skip' на экране {screen_count + 1}")
    test_passed = True

    # Пропускаем экраны
    for i in range(screen_count):
        logger.info(f"Экран {i + 1}: Проверка видимости кнопки 'Continue'")
        if not onboarding.is_continue_button_visible():
            logger.error(f"Кнопка 'Continue' не отображается на экране {i + 1}")
            test_passed = False
            break  # Если кнопка "Continue" не отображается, тест провален
        else:
            logger.info(f"Кнопка 'Continue' отображается на экране {i + 1}")

        logger.info(f"Экран {i + 1}: Нажатие на кнопку 'Continue'")
        onboarding.tap_continue()

    # Проверка кнопки 'Skip'
    if test_passed:  # Продолжаем, только если предыдущие шаги прошли успешно
        logger.info(f"Проверка видимости кнопки 'Skip' на экране {screen_count + 1}")
        if not onboarding.is_skip_button_visible():
            logger.error(f"Кнопка 'Skip' не отображается на экране {screen_count + 1}")
            test_passed = False
        else:
            logger.info(f"Кнопка 'Skip' отображается на экране {screen_count + 1}")

        logger.info("Нажатие на кнопку 'Skip'")
        onboarding.tap_skip()

        logger.info("Проверка видимости главного экрана")
        if not onboarding.is_main_screen_visible():
            logger.error("Главный экран не отображается после нажатия 'Skip'")
            test_passed = False
        else:
            logger.info("Главный экран отображается после нажатия 'Skip'")

    if test_passed:
        logger.info("Тест успешно завершен")
    else:
        logger.error("Тест завершился с ошибками")

    assert test_passed, "Тест завершился с ошибками (см. логи)"