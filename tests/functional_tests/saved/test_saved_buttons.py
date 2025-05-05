import pytest
import allure

@pytest.mark.saved
@pytest.mark.smoke
@allure.description("""
**Проверка log_in.**
""")
def test_log_in(logger, log_in, log_out):
    page = log_in
    page = log_out

@pytest.mark.saved
@pytest.mark.smoke
@allure.description("""
**Проверка работы кнопки 'select' на экране 'saved' (не залогированный аккаунт).**
""")
def test_select_button(pages, logger, skip_onboarding):
    """Тестирование кнопки 'select' на экране 'saved' в разделе 'more'"""
    try:
        saved = pages.saved
        logger.info("=== Начало теста: Проверка работы кнопки 'select' ===")

        with allure.step("1. Нажатие кнопки 'saved'"):
            assert saved.clicks.safe_click(saved.SAVED_BTN), "Кнопка 'saved' не найдена"
            logger.info("Кнопка 'saved' нажата")
            logger.debug("Проверяем, что мы на экране с предложением логина")
            assert saved.clicks.is_visible(saved.MESSAGE_TITLE_VIEW_TV), "Мы не на экране с предложением логина"
            logger.info("Находимся на экране с предложением логина")

        with allure.step("2. Нажатие кнопки 'more'"):
            assert saved.clicks.safe_click(saved.MORE_OPTIONS_BTN), "Кнопка 'more' не найдена"
            logger.info("Кнопка 'more' найдена и нажата")

        with allure.step("3. Нажатие кнопки 'select'"):
            logger.debug("Ищем кнопку 'select'")
            assert saved.clicks.safe_click(saved.SELECT_TV), "Кнопка 'select' не найдена"
            logger.info("Кнопка 'select' найдена и нажата")
            logger.debug("Проверяем, активность кнопки 'select' отобразилась на экране")
            assert saved.clicks.is_visible(saved.ACTION_MODE_BAR_VG), "Активность кнопки 'select' не отобразилась на экране"
            logger.info("Активность кнопки 'select' отобразилась на экране")

        with allure.step("4. Выход с активности кнопки 'select' с помощью кнопки 'Done'"):
            logger.debug("Ищем кнопку 'Done'")
            assert saved.clicks.safe_click(saved.DONE_IV), "Кнопка 'Done' не найдена"
            logger.info("Кнопка 'Done' найдена и нажата")
            logger.debug("Проверяем, что мы на экране с предложением логина")
            assert saved.clicks.is_visible(saved.MESSAGE_TITLE_VIEW_TV), "Мы не на экране с предложением логина"
            logger.info("Находимся на экране с предложением логина")

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.saved
@pytest.mark.smoke
@allure.description("""
**Проверка работы кнопки 'Filter_my_list' на экране 'saved' (не залогированный аккаунт).**
""")
def test_filter_my_list_button(pages, logger, skip_onboarding):
    """Тестирование кнопки 'filter_my_list' на экране 'saved'"""
    try:
        saved = pages.saved
        logger.info("=== Начало теста: Проверка работы кнопки 'filter_my_list' ===")

        with allure.step("1. Нажатие кнопки 'saved'"):
            assert saved.clicks.safe_click(saved.SAVED_BTN), "Кнопка 'saved' не найдена"
            logger.info("Кнопка 'saved' нажата")
            logger.debug("Проверяем, что мы на экране с предложением логина")
            assert saved.clicks.is_visible(saved.MESSAGE_TITLE_VIEW_TV), "Мы не на экране с предложением логина"
            logger.info("Находимся на экране с предложением логина")

        with allure.step("2. Нажатие кнопки 'Filter_my_list'"):
            assert saved.clicks.safe_click(saved.FILTER_MY_LISTS_BTN), "Кнопка 'Filter_my_list' не найдена"
            logger.info("Кнопка 'Filter_my_list' нажата")
            logger.debug("Проверяем, что мы на фильтрации листа")
            assert saved.clicks.is_visible(saved.DONE_IV), "Мы не на экране с фильтрацией листа"
            logger.info("Находимся на экране с фильтрацией листа")

        with allure.step("3. Поиск поля фильтрации для ввода текста"):
            logger.debug("Ищем поле для ввода текста 'search_src_text'")
            assert saved.clicks.is_visible(saved.SEARCH_SRC_TEXT_ACTV), "Поле 'search_src_text' не найдено"
            logger.info("Поле 'search_src_text' найдено")

        with allure.step("4. Ввод текста в поле фильтрации"):
            assert saved.test_text_input_works(), "Поле не найдено"

        with allure.step("5. Выход с экрана фильтрации с помощью кнопки 'Done'"):
            logger.debug("Ищем кнопку 'Done'")
            assert saved.clicks.safe_click(saved.DONE_IV), "Кнопка 'Done' не найдена"
            logger.info("Кнопка 'Done' найдена и нажата")
            logger.debug("Проверяем, что мы на экране с предложением логина")
            assert saved.clicks.is_visible(saved.MESSAGE_TITLE_VIEW_TV), "Мы не на экране с предложением логина"
            logger.info("Находимся на экране с предложением логина")

        logger.info("=== Тест успешно завершен ===")

    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.saved
@pytest.mark.smoke
@allure.description("""
**Проверка работы кнопки 'Not now' на экране 'saved' (не залогированный аккаунт).**
""")
def test_not_now_button(pages, logger, skip_onboarding):
    """Тестирование кнопки 'Not now' на экране 'saved'"""
    try:
        saved = pages.saved
        logger.info("=== Начало теста: Проверка работы кнопки 'Not now' ===")

        with allure.step("1. Нажатие кнопки 'saved'"):
            assert saved.clicks.safe_click(saved.SAVED_BTN), "Кнопка 'saved' не найдена"
            logger.info("Кнопка 'saved' нажата")
            logger.debug("Проверяем, что мы на экране с предложением логина")
            assert saved.clicks.is_visible(saved.MESSAGE_TITLE_VIEW_TV), "Мы не на экране логина"
            logger.info("Находимся на экране логина")

        with allure.step("2. Нажатие кнопки 'Not now'"):
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
**Проверка работы кнопки 'Log_in/join' на экране 'saved' (не залогированный аккаунт).**
""")
def test_log_in_button(pages, logger, skip_onboarding):
    """Тестирование кнопки 'Log_in/join' на экране 'saved'"""
    try:
        saved = pages.saved
        logger.info("=== Начало теста: Проверка работы кнопки 'Log_in/join' ===")

        with allure.step("1. Нажатие кнопки 'saved'"):
            assert saved.clicks.safe_click(saved.SAVED_BTN), "Кнопка 'saved' не найдена"
            logger.info("Кнопка 'saved' нажата")
            logger.debug("Проверяем, что мы на экране с предложением логина")
            assert saved.clicks.is_visible(saved.MESSAGE_TITLE_VIEW_TV), "Мы не на экране с предложением логина"
            logger.info("Находимся на экране с предложением логина")

        with allure.step("2. Нажатие кнопки 'Log_in/join'"):
            logger.debug("Ищем кнопку 'Log_in/join'")
            assert saved.clicks.safe_click(saved.POSITIVE_BTN), "Кнопка 'Log_in/join' не найдена"
            logger.info("Кнопка 'Log_in/join' найдена и нажата")
            logger.debug("Проверяем, что перешли на экран логина")
            assert saved.clicks.is_visible(saved.CREATE_AN_ACCOUNT_TV), "Мы не на экране логина"
            logger.info("Находимся на экране логина")

        with allure.step("3. Выход с экрана логина"):
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