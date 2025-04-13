import pytest
import logging
import os

# Создаем директорию для логов, если ее нет
log_dir = r""#нужно вставить путь до своего местоположения файла
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, 'test_onboarding_continue.log')

# Создаем логгер
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Создаем обработчик для записи в файл
file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8') # Указываем кодировку utf-8
file_handler.setLevel(logging.INFO)

# Создаем форматтер
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)

@pytest.mark.usefixtures("onboarding")  # Убедитесь, что фикстура onboarding определена
def test_continue_through_all_screens(onboarding, device_logs):
    """Тестирование кнопки 'Continue' на всех экранах онбординга"""

    logger.info("Начало теста 'Продолжение через все экраны онбординга'")

    test_passed = True  # Флаг для отслеживания успеха теста

    for i in range(3):
        logger.info(f"На экране {i + 1}: Проверка видимости кнопки 'Continue'")
        is_visible = onboarding.is_continue_button_visible()
        if not is_visible:
            logger.error(f"Кнопка 'Continue' не отображается на экране {i + 1}")
            test_passed = False  # Если хотя бы одна проверка не прошла, тест считается проваленным
        else:
            logger.info(f"Кнопка 'Continue' отображается на экране {i + 1}")

        logger.info(f"На экране {i + 1}: Нажатие на кнопку 'Continue'")
        onboarding.tap_continue()
        logger.info(f"Переход на следующий экран онбординга")

    logger.info("Проверка видимости кнопки 'Get Started'")
    is_get_started_visible = onboarding.is_get_started_visible()

    if not is_get_started_visible:
        logger.error("Кнопка 'Get Started' не отображается")
        test_passed = False
    else:
        logger.info("Кнопка 'Get Started' отображается")

    if test_passed:
        logger.info("Тест успешно завершен")
    else:
        logger.error("Тест завершился с ошибками")

    assert test_passed, "Тест завершился с ошибками (см. логи)"