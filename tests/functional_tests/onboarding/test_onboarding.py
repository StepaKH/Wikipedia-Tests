import pytest

@pytest.mark.onboarding
@pytest.mark.smoke
def test_add_or_edit_languages(onboarding, device_logs, logger):
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

@pytest.mark.onboarding
@pytest.mark.smoke
def test_continue_through_all_screens(onboarding, device_logs, logger):
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

@pytest.mark.onboarding
@pytest.mark.smoke
def test_get_started_button(onboarding, device_logs, logger):
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

@pytest.mark.onboarding
@pytest.mark.smoke
@pytest.mark.parametrize("screen_count", [0, 1, 2])
def test_skip_button_on_screens(onboarding, screen_count, device_logs, logger):
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