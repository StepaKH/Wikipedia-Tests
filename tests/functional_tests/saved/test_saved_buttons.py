import pytest
import allure

@pytest.mark.saved
@pytest.mark.smoke
@allure.description("""
**Проверка работы кнопки 'Not now' на экране 'saved'.**
""")
def test_not_now_button(pages, logger):
    """Тестирование кнопки 'Not now' на экране 'saved'"""
    try:
        saved = pages.saved.buttons
        logger.info("=== Начало теста: Проверка работы кнопки 'Not now' ===")

        with allure.step("1. Пропуск первых экранов"):
            for i in range(3):
                logger.debug(f"Пропускаем экран {i + 1}")
                assert saved.clicks.safe_click(saved.CONTINUE_BTN), f"Не удалось найти кнопку 'Continue' на экране {i + 1}"
            logger.info("Успешно пропущены 3 экрана онбординга")

        with allure.step("2. Нажатие кнопки 'Get Started'"):
            logger.debug("Ищем кнопку завершения онбординга")
            assert saved.clicks.safe_click(saved.GET_STARTED_BTN), "Кнопка 'Get Started' не найдена"
            logger.info("Кнопка 'Get Started' найдена и нажата")
            logger.debug("Проверяем наличие кнопки 'saved' на главном экране")
            assert saved.clicks.is_visible(saved.SAVED_BTN), "Кнопка 'saved' не найдена"
            logger.info("Мы на главном экране")

        with allure.step("3. Нажатие кнопки 'saved'"):
            assert saved.clicks.safe_click(saved.SAVED_BTN), "Кнопка 'saved' не найдена"
            logger.info("Кнопка 'saved' нажата")
            logger.debug("Проверяем, что мы на экране с предложением логина")
            assert saved.clicks.is_visible(saved.MESSAGE_TITLE_VIEW_TV), "Мы не на экране логина"
            logger.info("Находимся на экране логина")

        with allure.step("4. Нажатие кнопки 'Not now'"):
            logger.debug("Ищем кнопку 'Not now'")
            assert saved.clicks.safe_click(saved.NEGATIVE_BTN), "Кнопка 'Not now' не найдена"
            logger.info("Кнопка 'Not now' найдена и нажата")
            logger.debug("Проверяем, что предложение войти в аккаунт исчезло")
            assert saved.clicks.is_visible(saved.EMPTY_TITLE_TV), "Предложение войти в аккаунт не исчезло"
            logger.info("Предложение войти в аккаунт исчезло")

        logger.info("=== Тест успешно завершен ===")

    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.saved
@pytest.mark.smoke
@allure.description("""
**Проверка работы кнопки 'Log_in/join' на экране 'saved'.**
""")
def test_log_in_button(pages, logger):
    """Тестирование кнопки 'Log_in/join' на экране 'saved'"""
    try:
        saved = pages.saved.buttons
        logger.info("=== Начало теста: Проверка работы кнопки 'Log_in/join' ===")

        with allure.step("1. Пропуск первых экранов"):
            for i in range(3):
                logger.debug(f"Пропускаем экран {i + 1}")
                assert saved.clicks.safe_click(saved.CONTINUE_BTN), f"Не удалось найти кнопку 'Continue' на экране {i + 1}"
            logger.info("Успешно пропущены 3 экрана онбординга")

        with allure.step("2. Нажатие кнопки 'Get Started'"):
            logger.debug("Ищем кнопку завершения онбординга")
            assert saved.clicks.safe_click(saved.GET_STARTED_BTN), "Кнопка 'Get Started' не найдена"
            logger.info("Кнопка 'Get Started' найдена и нажата")
            logger.debug("Проверяем наличие кнопки 'saved' на главном экране")
            assert saved.clicks.is_visible(saved.SAVED_BTN), "Кнопка 'saved' не найдена"
            logger.info("Мы на главном экране")

        with allure.step("3. Нажатие кнопки 'saved'"):
            assert saved.clicks.safe_click(saved.SAVED_BTN), "Кнопка 'saved' не найдена"
            logger.info("Кнопка 'saved' нажата")
            logger.debug("Проверяем, что мы на экране с предложением логина")
            assert saved.clicks.is_visible(saved.MESSAGE_TITLE_VIEW_TV), "Мы не на экране с предложением логина"
            logger.info("Находимся на экране с предложением логина")

        with allure.step("4. Нажатие кнопки 'Log_in/join'"):
            logger.debug("Ищем кнопку 'Log_in/join'")
            assert saved.clicks.safe_click(saved.POSITIVE_BTN), "Кнопка 'Log_in/join' не найдена"
            logger.info("Кнопка 'Log_in/join' найдена и нажата")
            logger.debug("Проверяем, что перешли на экран логина")
            assert saved.clicks.is_visible(saved.CREATE_AN_ACCOUNT_TV), "Мы не на экране логина"
            logger.info("Находимся на экране логина")

        with allure.step("5. Выход с экрана логина"):
            logger.debug("Ищем кнопку 'navigate_up'")
            assert saved.clicks.safe_click(saved.NAVIGATE_UP_BTN), "Кнопка 'navigate_up' не найдена"
            logger.info("Кнопка 'navigate_up' найдена и нажата")
            logger.debug("Проверяем, что перешли на экран с предложением логина")
            assert saved.clicks.is_visible(saved.MESSAGE_TITLE_VIEW_TV), "Мы не на экране с предложением логина"
            logger.info("Находимся на экране с предложением логина")

        logger.info("=== Тест успешно завершен ===")

    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise