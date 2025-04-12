import pytest
import logging
import os

# Настройка логирования
log_dir = r""#нужно вставить путь до своего местоположения файла
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, 'test_onboarding_add_languages.log')

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
def test_add_or_edit_languages(onboarding, device_logs):
    """Тест кнопки 'Add or edit languages' и навигации обратно"""

    logger.info("Начало теста 'Add or edit languages' и навигации обратно")
    test_passed = True

    # Проверка кнопки 'Add or edit languages' на главном экране
    logger.info("Проверка видимости кнопки 'Add or edit languages' на главном экране")
    if not onboarding.is_add_language_button_visible():
        logger.error("Кнопка 'Add or edit languages' не отображается")
        test_passed = False
    else:
        logger.info("Кнопка 'Add or edit languages' отображается")
    logger.info("Нажатие на кнопку 'Add or edit languages'")
    onboarding.tap_add_language_button()

    # Нажимаем кнопку "Add language" в списке
    logger.info("Нажимаем кнопку 'Add language' в списке")
    if not onboarding.is_add_language_in_list_visible():
        logger.error("Кнопка 'Add language' не отображается")
        test_passed = False
    else:
        logger.info("Кнопка 'Add language' отображается")
    onboarding.tap_add_language_in_list()

    # Появляется кнопка "Navigate up" — возвращаемся на экран выбора языка
    logger.info("Проверка кнопки 'Navigate up' — возвращаемся на экран выбора языка")
    if not onboarding.is_navigate_up_visible():
        logger.error("Кнопка 'Navigate up' не отображается (1-й раз)")
        test_passed = False
    else:
        logger.info("Кнопка 'Navigate up' отображается (1-й раз)")
    onboarding.tap_navigate_up()

    # Возвращаемся на экран онбординга снова через "Navigate up"
    logger.info("Возвращаемся на экран онбординга снова через 'Navigate up'")
    if not onboarding.is_navigate_up_visible():
        logger.error("Кнопка 'Navigate up' не отображается (2-й раз)")
        test_passed = False
    else:
        logger.info("Кнопка 'Navigate up' отображается (2-й раз)")
    onboarding.tap_navigate_up()

    # Проверка, что вернулись на экран с кнопкой "Continue"
    logger.info("Проверка, что вернулись на экран с кнопкой 'Continue'")
    if not onboarding.is_continue_button_visible():
        logger.error("Кнопка 'Continue' не отображается — возможно, не вернулись на экран онбординга")
        test_passed = False
    else:
        logger.info("Кнопка 'Continue' отображается — вернулись на экран онбординга")

    if test_passed:
        logger.info("Тест успешно завершен")
    else:
        logger.error("Тест завершился с ошибками")

    assert test_passed, "Тест завершился с ошибками (см. логи)"