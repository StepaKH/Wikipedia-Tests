import pytest
import allure

@pytest.mark.onboarding
@pytest.mark.smoke
@allure.description("""
**Проверка навигации по экранам выбора языка в процессе онбординга.**
""")
def test_add_or_edit_languages(pages, logger):
    """Тест кнопки 'Add or edit languages' и навигации обратно"""
    try:
        onboarding = pages.onboarding.buttons
        logger.info("=== Начало теста: проверка кнопки 'Add or edit languages' ===")
        with allure.step("1. Нажать кнопку 'Add or edit languages' на стартовом экране онбординга → В приложении открывается экран выбора языков"):
            logger.debug("Проверяем видимость кнопки 'Add or edit languages'")
            assert onboarding.clicks.safe_click(onboarding.ADD_LANGUAGE_BTN), "Кнопка 'Add or edit languages' не найдена"
            logger.info("Кнопка 'Add or edit languages' найдена и нажата")
            logger.debug("Ищем кнопку 'Add language' в списке")
            assert onboarding.clicks.is_visible(onboarding.ADD_LANGUAGE_ITEM), "Кнопка в списке не найдена"
            logger.info("Находимся на экране выбора языков")

        with allure.step("2. Нажать кнопку 'Add language' на экране выбора языков → Открывается экран добавления нового языка"):
            onboarding.clicks.click(onboarding.ADD_LANGUAGE_ITEM)
            logger.info("Кнопка 'Add language' найдена и нажата")
            logger.debug("Проверяем кнопку 'Navigate up'")
            assert onboarding.clicks.is_visible(onboarding.NAVIGATE_UP_BTN), "Кнопка навигации не найдена"
            logger.info("Находимся на экране добавления нового языка")

        with allure.step("3. Выполнить возврат на экран выбора языков через системную кнопку навигации → Открывется экран выбора языков"):
            onboarding.clicks.click(onboarding.NAVIGATE_UP_BTN)
            logger.info("Кнопка 'Navigate up' найдена и нажата")
            logger.debug("Проверяем кнопку 'Navigate up'")
            assert onboarding.clicks.is_visible(onboarding.NAVIGATE_UP_BTN), "Кнопка навигации не найдена"
            logger.info("Вернулись на экран выбора языков")

        with allure.step("4. Выполнить возврат на экран онбординга через системную кнопку навигации → Открывется стартовый экран онбординга"):
            onboarding.clicks.click(onboarding.NAVIGATE_UP_BTN)
            logger.info("Кнопка 'Navigate up' найдена и нажата")
            logger.debug("Проверяем, что вернулись на экран онбординга")
            assert onboarding.clicks.is_visible(onboarding.CONTINUE_BTN), "Не вернулись на экран онбординга"
            logger.info("Вернулись на экран онбординга")

        logger.info("=== Тест успешно завершен ===")

    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.onboarding
@pytest.mark.smoke
@allure.description("""
**Проверка навигации по экранам онбординга с помощью кнопки 'Continue'.**
""")
def test_continue_through_all_screens(pages, logger):
    """Тестирование кнопки 'Continue' на всех экранах онбординга"""
    try:
        onboarding = pages.onboarding.buttons
        logger.info("=== Начало теста: проход по всем экранам онбординга ===")

        for i in range(3):
            with allure.step(f"{i + 1}. Экран {i + 1}"):
                logger.debug(f"Проверяем кнопку 'Continue' на экране {i + 1}")
                assert onboarding.clicks.safe_click(onboarding.CONTINUE_BTN), f"Кнопка не найдена на экране {i + 1}"
                logger.info(f"Кнопка 'Continue' найдена и нажата на экране {i + 1}")

        with allure.step("4. Проверка финального экрана"):
            logger.debug("Проверяем кнопку 'Get Started'")
            assert onboarding.clicks.is_visible(onboarding.GET_STARTED_BTN), "Кнопка 'Get Started' не найдена"
            logger.info("Все экраны пройдены успешно")

        logger.info("=== Тест успешно завершен ===")

    except Exception as e:
        logger.error(f"!!! Тест упал на экране {i + 1}: {str(e)}")
        raise

@pytest.mark.onboarding
@pytest.mark.smoke
@allure.description("""
**Проверка работы кнопки 'Get Started' на финальном экране онбординга.**
""")
def test_get_started_button(pages, logger):
    """Тестирование кнопки 'Get Started' на последнем экране онбординга"""
    try:
        onboarding = pages.onboarding.buttons
        logger.info("=== Начало теста: проверка кнопки 'Get Started' ===")

        with allure.step("1. Пропуск первых экранов"):
            for i in range(3):
                logger.debug(f"Пропускаем экран {i + 1}")
                assert onboarding.clicks.safe_click(onboarding.CONTINUE_BTN), f"Не удалось найти кнопку 'Continue' на экране {i + 1}"
            logger.info("Успешно пропущены 3 экрана онбординга")

        with allure.step("2. Проверка кнопки 'Get Started'"):
            logger.debug("Ищем кнопку завершения онбординга")
            assert onboarding.clicks.safe_click(onboarding.GET_STARTED_BTN), "Кнопка 'Get Started' не найдена"
            logger.info("Кнопка 'Get Started' найдена и нажата")
            logger.debug("Проверяем отображение главного экрана")
            assert onboarding.clicks.is_visible(onboarding.MAIN_SCREEN), "Главный экран не отобразился"
            logger.info("Успешный переход на главный экран")

        logger.info("=== Тест успешно завершен ===")

    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.onboarding
@pytest.mark.smoke
@pytest.mark.parametrize("screen_count", [0, 1, 2])
@allure.description("""
**Параметризованный тест проверки кнопки 'Skip' на разных экранах онбординга.**
""")
def test_skip_button_on_screens(pages, screen_count, logger):
    """Проверка кнопки 'Skip' на разных экранах онбординга"""
    try:
        onboarding = pages.onboarding.buttons
        logger.info(f"=== Начало теста: проверка кнопки 'Skip' (экран {screen_count + 1}) ===")

        with allure.step("1. Навигация до целевого экрана"):
            for i in range(screen_count):
                logger.debug(f"Переход через экран {i + 1}")
                assert onboarding.clicks.safe_click(onboarding.CONTINUE_BTN), f"Не удалось найти кнопку Continue на экране {i + 1}"
            logger.info(f"Успешно достигнут экран {screen_count + 1}")

        with allure.step("2. Проверка кнопки 'Skip'"):
            logger.debug("Ищем кнопку пропуска онбординга")
            assert onboarding.clicks.safe_click(onboarding.SKIP_BTN), "Кнопка 'Skip' не найдена"
            logger.info("Кнопка найдена и нажата")
            logger.debug("Проверяем отображение главного экрана")
            assert onboarding.clicks.is_visible(onboarding.MAIN_SCREEN), "Главный экран не отобразился"
            logger.info("Успешный переход на главный экран")

        logger.info("=== Тест успешно завершен ===")

    except Exception as e:
        logger.error(f"!!! Тест упал на экране {screen_count + 1}: {str(e)}")
        raise