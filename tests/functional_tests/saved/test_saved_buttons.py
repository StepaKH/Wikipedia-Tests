import pytest
import allure

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

        with allure.step("2. Создаем 3 листа для теста фильтра на экране 'saved'"):
            assert saved.create_list(), "Не удалось создать первый лист"
            logger.info("Создали первый лист")
            assert saved.create_list(), "Не удалось создать второй лист"
            logger.info("Создали второй лист")
            assert saved.create_list(), "Не удалось создать третий лист"
            logger.info("Создали третий лист")

        with allure.step("3. Нажатие кнопки 'Filter_my_list'"):
            assert saved.clicks.safe_click(saved.FILTER_MY_LISTS_BTN), "Кнопка 'Filter_my_list' не найдена"
            logger.info("Кнопка 'Filter_my_list' нажата")
            logger.debug("Проверяем, что мы на фильтрации листа")
            assert saved.clicks.is_visible(saved.DONE_IV), "Мы не на экране с фильтрацией листа"
            logger.info("Находимся на экране с фильтрацией листа")

        with allure.step("4. Поиск поля фильтрации для ввода текста"):
            logger.debug("Ищем поле для ввода текста 'search_src_text'")
            assert saved.clicks.is_visible(saved.SEARCH_SRC_TEXT_ACTV), "Поле 'search_src_text' не найдено"
            logger.info("Поле 'search_src_text' найдено")

        with allure.step("5. Ввод текста в поле фильтрации"):
            assert saved.test_text_input_works(), "Поле не найдено"

        with allure.step("4. Проверка, что фильтр отработала корректно"):
            actual = saved.get_list_names()
            expected = [saved.test_primary[2]]
            logger.debug(f"Actual: {actual}")
            logger.debug(f"Expected: {expected}")
            assert actual == expected, "Фильтр сработал неверно"
            logger.info("Фильтр сработал верно")

        with allure.step("5. Выход с экрана фильтрации с помощью кнопки 'Done'"):
            logger.debug("Ищем кнопку 'Done'")
            assert saved.clicks.safe_click(saved.DONE_IV), "Кнопка 'Done' не найдена"
            logger.info("Кнопка 'Done' найдена и нажата")
            logger.debug("Проверяем, что мы на экране с предложением логина")
            assert saved.clicks.is_visible(saved.MESSAGE_TITLE_VIEW_TV), "Мы не на экране с предложением логина"
            logger.info("Находимся на экране с предложением логина")

        logger.info("=== Тест успешно завершен ===")
        saved.delete_array()
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.saved
@pytest.mark.smoke
@allure.description("""
**Проверка сортировки листов. (не залогированный аккаунт)**
""")
def test_sort_by(pages, logger, skip_onboarding):
    """Тестирование работы сортировки"""
    try:
        saved = pages.saved
        with allure.step("1. Нажатие кнопки 'saved'"):
            assert saved.clicks.safe_click(saved.SAVED_BTN), "Кнопка 'saved' не найдена"
            logger.info("Кнопка 'saved' нажата")
            logger.debug("Проверяем, что мы на экране с предложением логина")
            assert saved.clicks.is_visible(saved.MESSAGE_TITLE_VIEW_TV), "Мы не на экране с предложением логина"
            logger.info("Находимся на экране с предложением логина")

        with allure.step("2. Создаем 3 листа для теста их сортировки на экране 'saved'"):
            assert saved.create_list(), "Не удалось создать первый лист"
            logger.info("Создали первый лист")
            assert saved.create_list(), "Не удалось создать второй лист"
            logger.info("Создали второй лист")
            assert saved.create_list(), "Не удалось создать третий лист"
            logger.info("Создали третий лист")

        logger.info("=== Начало теста: Проверка работы кнопки 'sort_by_name(reverse)' ===")
        with allure.step("3. Нажатие кнопки 'sort_by_name(reverse)'"):
            logger.info("Нажатие кнопки 'more'")
            assert saved.clicks.safe_click(saved.MORE_OPTIONS_BTN), "Кнопка 'more' не найдена"
            logger.info("Кнопка 'more' найдена и нажата")
            logger.info("Нажатие кнопки 'sort_by'")
            assert saved.clicks.safe_click(saved.SORT_BY_TV), "Кнопка 'sort_by' не найдена"
            logger.info("Кнопка 'sort_by' найдена и нажата")
            logger.info("Нажатие кнопки 'sort_by_name (reverse)'")
            assert saved.clicks.safe_click(saved.SORT_BY_NAME_REVERSE_TV), "Кнопка 'sort_by_name (reverse)' не найдена"
            logger.info("Кнопка 'sort_by_name (reverse)' найдена и нажата")

        with allure.step("4. Проверка, что 'sort_by_name(reverse)' отработала корректно"):
            actual = saved.get_list_names()
            expected = saved.reverse_sort_array_by_name()
            logger.debug(f"Actual: {actual}")
            logger.debug(f"Expected: {expected}")
            assert actual == expected, "Кнопка 'sort_by_name (reverse)' сработала неверно"
            logger.info("Кнопка 'sort_by_name (reverse)' сработала верно")

        logger.info("=== Начало теста: Проверка работы кнопки 'sort_by_name' ===")
        with allure.step("4. Нажатие кнопки 'sort_by_name'"):
            logger.info("Нажатие кнопки 'more'")
            assert saved.clicks.safe_click(saved.MORE_OPTIONS_BTN), "Кнопка 'more' не найдена"
            logger.info("Кнопка 'more' найдена и нажата")
            logger.info("Нажатие кнопки 'sort_by'")
            assert saved.clicks.safe_click(saved.SORT_BY_TV), "Кнопка 'sort_by' не найдена"
            logger.info("Кнопка 'sort_by' найдена и нажата")
            logger.info("Нажатие кнопки 'sort_by_name'")
            assert saved.clicks.safe_click(saved.SORT_BY_NAME_TV), "Кнопка 'sort_by_name' не найдена"
            logger.info("Кнопка 'sort_by_name' найдена и нажата")

        with allure.step("5. Проверка, что 'sort_by_name' отработала корректно"):
            actual = saved.get_list_names()
            expected = saved.sort_array_by_name()
            logger.debug(f"Actual: {actual}")
            logger.debug(f"Expected: {expected}")
            assert actual == expected, "Кнопка 'sort_by_name' сработала неверно"
            logger.info("Кнопка 'sort_by_name' сработала верно")

        logger.info("=== Начало теста: Проверка работы кнопки 'sort_by_data_oldest' ===")
        with allure.step("6. Нажатие кнопки 'sort_by_data_oldest'"):
            logger.info("Нажатие кнопки 'more'")
            assert saved.clicks.safe_click(saved.MORE_OPTIONS_BTN), "Кнопка 'more' не найдена"
            logger.info("Кнопка 'more' найдена и нажата")
            logger.info("Нажатие кнопки 'sort_by'")
            assert saved.clicks.safe_click(saved.SORT_BY_TV), "Кнопка 'sort_by' не найдена"
            logger.info("Кнопка 'sort_by' найдена и нажата")
            logger.info("Нажатие кнопки 'sort_by_data_oldest'")
            assert saved.clicks.safe_click(saved.SORT_BY_DATE_CREATED_OLDEST_TV), "Кнопка 'sort_by_data_oldest' не найдена"
            logger.info("Кнопка 'sort_by_data_oldest' найдена и нажата")

        with allure.step("7. Проверка, что 'sort_by_data_oldest' отработала корректно"):
            actual = saved.get_list_names()
            expected = saved.sort_array_by_data()
            logger.debug(f"Actual: {actual}")
            logger.debug(f"Expected: {expected}")
            assert actual == expected, "Кнопка 'sort_by_data_oldest' сработала неверно"
            logger.info("Кнопка 'sort_by_data_oldest' сработала верно")

        logger.info("=== Начало теста: Проверка работы кнопки 'sort_by_data_newest' ===")
        with allure.step("8. Нажатие кнопки 'sort_by_data_newest'"):
            logger.info("Нажатие кнопки 'more'")
            assert saved.clicks.safe_click(saved.MORE_OPTIONS_BTN), "Кнопка 'more' не найдена"
            logger.info("Кнопка 'more' найдена и нажата")
            logger.info("Нажатие кнопки 'sort_by'")
            assert saved.clicks.safe_click(saved.SORT_BY_TV), "Кнопка 'sort_by' не найдена"
            logger.info("Кнопка 'sort_by' найдена и нажата")
            logger.info("Нажатие кнопки 'sort_by_data_newest'")
            assert saved.clicks.safe_click(saved.SORT_BY_DATE_CREATED_NEWEST_TV), "Кнопка 'sort_by_data_newest' не найдена"
            logger.info("Кнопка 'sort_by_data_newest' найдена и нажата")

        with allure.step("9. Проверка, что 'sort_by_data_newest' отработала корректно"):
            actual = saved.get_list_names()
            expected = saved.reverse_sort_array_by_data()
            logger.debug(f"Actual: {actual}")
            logger.debug(f"Expected: {expected}")
            assert actual == expected, "Кнопка 'sort_by_data_newest' сработала неверно"
            logger.info("Кнопка 'sort_by_data_newest' сработала верно")
        logger.info("=== Тест успешно завершен ===")
        saved.delete_array()
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.saved
@pytest.mark.smoke
@allure.description("""
**Проверка работы кнопки 'refresh_sync'. (залогированный аккаунт)**
""")
def test_refresh_sync(logger, log_in, log_out):
    """Тестирование работы кнопки 'refresh_sync'"""
    try:
        logger.info("=== Начало теста: Проверка работы кнопки 'refresh_sync' ===")
        saved = log_in
        with allure.step("1. Нажатие кнопки 'more'"):
            assert saved.clicks.safe_click(saved.MORE_OPTIONS_BTN), "Кнопка 'more' не найдена"
            logger.info("Кнопка 'more' найдена и нажата")

        with allure.step("2. Нажатие кнопки 'refresh_sync'"):
            logger.debug("Ищем кнопку 'refresh_sync'")
            assert saved.clicks.safe_click(saved.REFRESH_SYNC_TV), "Кнопка 'refresh_sync' не найдена"
            logger.info("Кнопка 'refresh_sync' найдена и нажата")
            assert saved.clicks.is_visible(saved.SNACKBAR_TEXT_TV), "Не удалось выполнить refresh_sync"
            logger.info("refresh_sync успешно выполнен")

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.saved
@pytest.mark.smoke
@allure.description("""
**Проверка уведомлений. (залогированный аккаунт)**
""")
def test_notifications(logger, log_in, log_out):
    """Тестирование работы уведомлений"""
    try:

        logger.info("=== Начало теста: Проверка уведомлений ===")
        saved = log_in

        with allure.step("1. Нажатие иконки колокольчика"):
            assert saved.clicks.safe_click(saved.NOTIFICATIONS_BTN), "Иконка колокольчика не найдена"
            logger.info("Иконка колокольчика найдена")
            logger.debug("Проверяем, что мы на экране уведомлений")
            assert saved.clicks.is_visible(saved.NAVIGATE_UP_BTN), "Мы не на экране уведомлений"
            logger.info("Мы на экране уведомлений")

        with allure.step("2. Переход между разделами уведомлений"):
            assert saved.clicks.safe_click(saved.MENTIONS_NTF_BTN), "Раздел mentions не найден"
            logger.info("Нашли раздел mentions и перешли в него")
            assert saved.clicks.safe_click(saved.ALL_NTF_BTN), "Раздел all не найден"
            logger.info("Нашли раздел all и перешли в него")

        with allure.step("3. Выход с экрана уведомлений"):
            assert saved.clicks.safe_click(saved.NAVIGATE_UP_BTN), "Кнопка выхода не найдена"
            logger.info("Вышли с экрана уведомлений")

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.saved
@pytest.mark.smoke
@allure.description("""
**Проверка работы шэйра листа на экране 'saved' через кнопку 'share' (не залогированный аккаунт).**
""")
def test_share_list_button(pages, logger, skip_onboarding):
    """Тестирование работы экспорта листа на экране 'saved' через кнопку 'export'"""
    try:
        saved = pages.saved
        logger.info("=== Начало теста: Проверка работы шэйра листа на экране 'saved' через кнопку 'share' ===")

        with allure.step("1. Нажатие кнопки 'saved'"):
            assert saved.clicks.safe_click(saved.SAVED_BTN), "Кнопка 'saved' не найдена"
            logger.info("Кнопка 'saved' нажата")
            logger.debug("Проверяем, что мы на экране с предложением логина")
            assert saved.clicks.is_visible(saved.MESSAGE_TITLE_VIEW_TV), "Мы не на экране с предложением логина"
            logger.info("Находимся на экране с предложением логина")

        with allure.step("2. Создаем лист для теста его изменения на экране 'saved'"):
            assert saved.create_list(), "Не удалось создать лист"

        with allure.step("3. Шэйр листа с помощью кнопки 'share'"):
            saved.press_to_title_activity()
            assert saved.clicks.is_visible(saved.SHARE_TV), "Не удалось сделать долгое нажатие на лист"
            logger.info("Появился список активностей для листа")
            assert saved.clicks.safe_click(saved.SHARE_TV), "Кнопка 'share' не найдена"
            logger.info("Кнопка 'share' нажата")
            assert saved.clicks.is_visible(saved.BLUETOOTH_TV), "Не удалось поделиться лист"
            logger.info("Успешно перешли на выбор того через что поделимся листом")
            saved.swipes.swipe_down()
            saved.swipes.swipe_down()
            logger.debug("Проверяем, что мы на экране с предложением логина")
            assert saved.clicks.is_visible(saved.MESSAGE_TITLE_VIEW_TV), "Мы не на экране с предложением логина"
            logger.info("Находимся на экране с предложением логина")

        logger.info("=== Тест успешно завершен ===")
        saved.delete_array()
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.saved
@pytest.mark.smoke
@allure.description("""
**Проверка работы экспорта листа на экране 'saved' через кнопку 'export' (не залогированный аккаунт).**
""")
def test_export_list_button(pages, logger, skip_onboarding):
    """Тестирование работы экспорта листа на экране 'saved' через кнопку 'export'"""
    try:
        saved = pages.saved
        logger.info("=== Начало теста: Проверка работы экспорта листа с помощью кнопки 'export' ===")

        with allure.step("1. Нажатие кнопки 'saved'"):
            assert saved.clicks.safe_click(saved.SAVED_BTN), "Кнопка 'saved' не найдена"
            logger.info("Кнопка 'saved' нажата")
            logger.debug("Проверяем, что мы на экране с предложением логина")
            assert saved.clicks.is_visible(saved.MESSAGE_TITLE_VIEW_TV), "Мы не на экране с предложением логина"
            logger.info("Находимся на экране с предложением логина")

        with allure.step("2. Создаем лист для теста его изменения на экране 'saved'"):
            assert saved.create_list(), "Не удалось создать лист"

        with allure.step("3. Экспорт листа с помощью кнопки 'export'"):
            saved.press_to_title_activity()
            assert saved.clicks.is_visible(saved.EXPORT_LIST_TV), "Не удалось сделать долгое нажатие на лист"
            logger.info("Появился список активностей для листа")
            assert saved.clicks.safe_click(saved.EXPORT_LIST_TV), "Кнопка 'export' не найдена"
            logger.info("Кнопка 'export' нажата")
            assert saved.clicks.is_visible(saved.SNACKBAR_TEXT_TV), "Не удалось экспортировать лист"
            logger.info("Лист успешно экспортирован")

        logger.info("=== Тест успешно завершен ===")
        saved.delete_array()
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.saved
@pytest.mark.smoke
@allure.description("""
**Проверка работы изменения названия и description листа на экране 'saved' через 'edit_list' (не залогированный аккаунт).**
""")
def test_edit_list_button(pages, logger, skip_onboarding):
    """Тестирование работы изменения названия и description листа на экране 'saved' через 'edit_list'"""
    try:
        saved = pages.saved
        logger.info("=== Начало теста: Проверка работы изменения листа с помощью кнопки 'edit_list' ===")

        with allure.step("1. Нажатие кнопки 'saved'"):
            assert saved.clicks.safe_click(saved.SAVED_BTN), "Кнопка 'saved' не найдена"
            logger.info("Кнопка 'saved' нажата")
            logger.debug("Проверяем, что мы на экране с предложением логина")
            assert saved.clicks.is_visible(saved.MESSAGE_TITLE_VIEW_TV), "Мы не на экране с предложением логина"
            logger.info("Находимся на экране с предложением логина")

        with allure.step("2. Создаем лист для теста его изменения на экране 'saved'"):
            assert saved.create_list(), "Не удалось создать лист"

        with allure.step("3. Изменение листа с помощью кнопки 'select'"):
            saved.press_to_title_activity()
            assert saved.clicks.is_visible(saved.EDIT_NAME_DESCRIPTION_TV), "Не удалось сделать долгое нажатие на лист"
            logger.info("Появился список активностей для листа")
            assert saved.clicks.safe_click(saved.EDIT_NAME_DESCRIPTION_TV), "Кнопка 'edit_list' не найдена"
            logger.info("Кнопка 'edit_list' нажата")
            assert saved.test_text_input_for_create_new_list(), "Не удалось изменить лист"
            logger.info("Данные изменены успешно")

        with allure.step("4. Нажатие кнопки 'ok'"):
            assert saved.clicks.safe_click(saved.OK_BUTTON1_BTN), "Кнопка 'ok' не найдена"
            logger.info("Кнопка 'ok' нажата")

        with allure.step("5. Проверяем, что лист изменился"):
            if saved.check_add_list():
                logger.info("Лист изменился")
            else: logger.info("Лист не изменился")

        logger.info("=== Тест успешно завершен ===")
        saved.delete_array()
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.saved
@pytest.mark.smoke
@allure.description("""
**Проверка работы удаления листа на экране 'saved' через 'select' (не залогированный аккаунт).**
""")
def test_delete_list_with_select_button(pages, logger, skip_onboarding):
    """Тестирование удаления листа на экране 'saved' через 'select'"""
    try:
        saved = pages.saved
        logger.info("=== Начало теста: Проверка работы удаления листа с помощью кнопки 'select' ===")

        with allure.step("1. Нажатие кнопки 'saved'"):
            assert saved.clicks.safe_click(saved.SAVED_BTN), "Кнопка 'saved' не найдена"
            logger.info("Кнопка 'saved' нажата")
            logger.debug("Проверяем, что мы на экране с предложением логина")
            assert saved.clicks.is_visible(saved.MESSAGE_TITLE_VIEW_TV), "Мы не на экране с предложением логина"
            logger.info("Находимся на экране с предложением логина")

        with allure.step("2. Создаем лист для теста его удаления на экране 'saved'"):
            assert saved.create_list(), "Не удалось создать лист"

        with allure.step("3. Удаление листа с помощью кнопки 'select'"):
            saved.press_to_title_activity()
            assert saved.clicks.is_visible(saved.SELECT_1_TV), "Не удалось сделать долгое нажатие на лист"
            logger.info("Появился список активностей для листа")
            assert saved.clicks.safe_click(saved.SELECT_1_TV), "Кнопка 'select' не найдена"
            logger.info("Кнопка 'select' нажата")
            assert saved.clicks.safe_click(saved.DELETE_SELECT_ITEMS_BTN), "Активность кнопки 'select' не найдена"
            logger.info("Кнопка 'мусорки' нажата")
            assert saved.clicks.safe_click(saved.OK_BUTTON1_BTN), "Кнопка 'delete' не найдена"
            logger.info("Кнопка 'delete' нажата")

        with allure.step("4. Проверяем, что лист удалился"):
            if saved.clicks.is_visible(saved.SNACKBAR_TEXT_TV):
                logger.info("Лист удалился")
            else: logger.info("Лист не удалился")

        logger.info("=== Тест успешно завершен ===")
        saved.delete_array()
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.saved
@pytest.mark.smoke
@allure.description("""
**Проверка работы удаления листа на экране 'saved' (не залогированный аккаунт).**
""")
def test_delete_list_with_delete_button(pages, logger, skip_onboarding):
    """Тестирование удаления листа на экране 'saved'"""
    try:
        saved = pages.saved
        logger.info("=== Начало теста: Проверка работы удаления листа с помощью кнопки 'delete' ===")

        with allure.step("1. Нажатие кнопки 'saved'"):
            assert saved.clicks.safe_click(saved.SAVED_BTN), "Кнопка 'saved' не найдена"
            logger.info("Кнопка 'saved' нажата")
            logger.debug("Проверяем, что мы на экране с предложением логина")
            assert saved.clicks.is_visible(saved.MESSAGE_TITLE_VIEW_TV), "Мы не на экране с предложением логина"
            logger.info("Находимся на экране с предложением логина")

        with allure.step("2. Создаем лист для теста его удаления на экране 'saved'"):
            assert saved.create_list(), "Не удалось создать лист"

        with allure.step("3. Удаление листа с помощью кнопки 'delete'"):
            saved.press_to_title_activity()
            assert saved.clicks.is_visible(saved.DELETE_LIST_TV), "Не удалось сделать долгое нажатие на лист"
            logger.info("Появился список активностей для листа")
            assert saved.clicks.safe_click(saved.DELETE_LIST_TV), "Кнопка 'delete' не найдена"
            logger.info("Кнопка 'delete' нажата")
            assert saved.clicks.safe_click(saved.OK_BUTTON1_BTN), "Кнопка 'ok' не найдена"
            logger.info("Кнопка 'ok' нажата")

        with allure.step("4. Проверяем, что лист удалился"):
            if saved.clicks.is_visible(saved.SNACKBAR_TEXT_TV):
                logger.info("Лист удалился")
            else: logger.info("Лист не удалился")

        logger.info("=== Тест успешно завершен ===")
        saved.delete_array()
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.saved
@pytest.mark.smoke
@allure.description("""
**Проверка работы кнопки 'create_new_list' на экране 'saved' (не залогированный аккаунт).**
""")
def test_create_new_list_button(pages, logger, skip_onboarding):
    """Тестирование кнопки 'create_new_list' на экране 'saved' в разделе 'more'"""
    try:
        saved = pages.saved
        logger.info("=== Начало теста: Проверка работы кнопки 'create_new_list' - 'cancel' ===")

        with allure.step("1. Нажатие кнопки 'saved'"):
            assert saved.clicks.safe_click(saved.SAVED_BTN), "Кнопка 'saved' не найдена"
            logger.info("Кнопка 'saved' нажата")
            logger.debug("Проверяем, что мы на экране с предложением логина")
            assert saved.clicks.is_visible(saved.MESSAGE_TITLE_VIEW_TV), "Мы не на экране с предложением логина"
            logger.info("Находимся на экране с предложением логина")

        with allure.step("2. Нажатие кнопки 'more'"):
            assert saved.clicks.safe_click(saved.MORE_OPTIONS_BTN), "Кнопка 'more' не найдена"
            logger.info("Кнопка 'more' найдена и нажата")

        with allure.step("3. Нажатие кнопки 'create_new_list'"):
            logger.debug("Ищем кнопку 'create_new_list'")
            assert saved.clicks.safe_click(saved.CREATE_NEW_LIST_TV), "Кнопка 'create_new_list' не найдена"
            logger.info("Кнопка 'create_new_list' найдена и нажата")
            logger.debug("Проверяем, что экран кнопки 'create_new_list' отобразился на экране")
            assert saved.clicks.is_visible(saved.TEXT_INPUT_ET), "Экран кнопки 'create_new_list' не отобразился на экране"
            logger.info("Экран кнопки 'create_new_list' отобразился на экране")

        with allure.step("4. Нажатие кнопки 'cancel'"):
            assert saved.clicks.safe_click(saved.CANCEL_BUTTON2_BTN), "Кнопка 'cancel' не найдена"
            logger.info("Кнопка 'cancel' нажата")
            logger.debug("Проверяем, что мы на экране с предложением логина")
            assert saved.clicks.is_visible(saved.MESSAGE_TITLE_VIEW_TV), "Мы не на экране с предложением логина"
            logger.info("Находимся на экране с предложением логина")

        logger.info("=== Начало теста: Проверка работы кнопки 'create_new_list' - 'ok' ===")

        with allure.step("5. Нажатие кнопки 'more'"):
            assert saved.clicks.safe_click(saved.MORE_OPTIONS_BTN), "Кнопка 'more' не найдена"
            logger.info("Кнопка 'more' найдена и нажата")

        with allure.step("6. Нажатие кнопки 'create_new_list'"):
            logger.debug("Ищем кнопку 'create_new_list'")
            assert saved.clicks.safe_click(saved.CREATE_NEW_LIST_TV), "Кнопка 'create_new_list' не найдена"
            logger.info("Кнопка 'create_new_list' найдена и нажата")
            logger.debug("Проверяем, что экран кнопки 'create_new_list' отобразился на экране")
            assert saved.clicks.is_visible(
                saved.TEXT_INPUT_ET), "Экран кнопки 'create_new_list' не отобразился на экране"
            logger.info("Экран кнопки 'create_new_list' отобразился на экране")

        with allure.step("7. Ввод данных названий в лист (основное и description)"):
            assert saved.test_text_input_for_create_new_list(), "Не удалось ввести данные"
            logger.info("Данные введены успешно")

        with allure.step("8. Нажатие кнопки 'ok'"):
            assert saved.clicks.safe_click(saved.OK_BUTTON1_BTN), "Кнопка 'ok' не найдена"
            logger.info("Кнопка 'ok' нажата")
            logger.debug("Проверяем, что лист с введенными названиями добавился")
            assert saved.check_add_list(), "Лист с введенными названиями не добавился"
            logger.info("Лист с введенными названиями добавился")

        logger.info("=== Тест успешно завершен ===")
        saved.delete_array()
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.saved
@pytest.mark.smoke
@allure.description("""
**Проверка работы кнопки 'import_list' на экране 'saved' (не залогированный аккаунт).**
""")
def test_import_list_button(pages, logger, skip_onboarding):
    """Тестирование кнопки 'import_list' на экране 'saved' в разделе 'more'"""
    try:
        saved = pages.saved
        logger.info("=== Начало теста: Проверка работы кнопки 'import_list' ===")

        with allure.step("1. Нажатие кнопки 'saved'"):
            assert saved.clicks.safe_click(saved.SAVED_BTN), "Кнопка 'saved' не найдена"
            logger.info("Кнопка 'saved' нажата")
            logger.debug("Проверяем, что мы на экране с предложением логина")
            assert saved.clicks.is_visible(saved.MESSAGE_TITLE_VIEW_TV), "Мы не на экране с предложением логина"
            logger.info("Находимся на экране с предложением логина")

        with allure.step("2. Нажатие кнопки 'more'"):
            assert saved.clicks.safe_click(saved.MORE_OPTIONS_BTN), "Кнопка 'more' не найдена"
            logger.info("Кнопка 'more' найдена и нажата")

        with allure.step("3. Нажатие кнопки 'import_list'"):
            logger.debug("Ищем кнопку 'import_list'")
            assert saved.clicks.safe_click(saved.IMPORT_LIST_TV), "Кнопка 'import_list' не найдена"
            logger.info("Кнопка 'import_list' найдена и нажата")
            logger.debug("Проверяем, что экран кнопки 'import_list' отобразился на экране")
            assert saved.clicks.is_visible(saved.LARGE_FILES_BTN), "Экран кнопки 'import_list' не отобразился на экране"
            logger.info("Экран кнопки 'import_list' отобразился на экране")

        with allure.step("4. Выход с экрана кнопки 'import_list' с помощью свайпа"):
            saved.swipes.swipe_right(speed = "fast")
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
**Проверка работы активности 'select' на экране 'saved' (не залогированный аккаунт).**
""")
def test_select_button(pages, logger, skip_onboarding):
    """Тестирование кнопки 'select' на экране 'saved' в разделе 'more'"""
    try:
        saved = pages.saved
        logger.info("=== Начало теста: Проверка работы активности 'select' через удаление листа ===")

        with allure.step("1. Нажатие кнопки 'saved'"):
            assert saved.clicks.safe_click(saved.SAVED_BTN), "Кнопка 'saved' не найдена"
            logger.info("Кнопка 'saved' нажата")
            logger.debug("Проверяем, что мы на экране с предложением логина")
            assert saved.clicks.is_visible(saved.MESSAGE_TITLE_VIEW_TV), "Мы не на экране с предложением логина"
            logger.info("Находимся на экране с предложением логина")

        with allure.step("2. Создаем лист для теста 'select' на экране 'saved'"):
            assert saved.create_list(), "Не удалось создать лист"

        with allure.step("3. Нажатие кнопки 'more'"):
            assert saved.clicks.safe_click(saved.MORE_OPTIONS_BTN), "Кнопка 'more' не найдена"
            logger.info("Кнопка 'more' найдена и нажата")

        with allure.step("4. Нажатие кнопки 'select'"):
            logger.debug("Ищем кнопку 'select'")
            assert saved.clicks.safe_click(saved.SELECT_TV), "Кнопка 'select' не найдена"
            logger.info("Кнопка 'select' найдена и нажата")
            logger.debug("Проверяем, активность кнопки 'select' отобразилась на экране")
            assert saved.clicks.is_visible(saved.CHECK_ALL_ITEMS_BTN), "Активность кнопки 'select' не отобразилась на экране"
            logger.info("Активность кнопки 'select' отобразилась на экране с пустым чекбоксом")

        with allure.step("5. Нажатие на чекбокс для его теста с помощью удаления"):
            assert saved.clicks.safe_click(saved.CHECK_ALL_ITEMS_BTN), "Пустой чекбокс не найден"
            assert saved.clicks.is_visible(saved.UNCHECK_ALL_ITEMS_BTN), "Не удалось нажать на чекбокс"
            logger.info("Теперь чекбокс заполненный и все элементы выбраны")
            assert saved.clicks.safe_click(saved.DELETE_SELECT_ITEMS_BTN), "Активность кнопки 'select' не найдена"
            logger.info("Кнопка 'мусорки' нажата")
            assert saved.clicks.safe_click(saved.OK_BUTTON1_BTN), "Кнопка 'delete' не найдена"
            logger.info("Кнопка 'delete' нажата")

        with allure.step("6. Проверяем, что лист удалился"):
            if saved.clicks.is_visible(saved.SNACKBAR_TEXT_TV):
                logger.info("Лист удалился, 'select' работает исправно")
            else: logger.info("Лист не удалился, 'select' работает не исправно")

        logger.info("=== Начало доп теста: Проверка работы возврата с активности 'select' через 'Done' ===")

        with allure.step("7. Нажатие кнопки 'more'"):
            assert saved.clicks.safe_click(saved.MORE_OPTIONS_BTN), "Кнопка 'more' не найдена"
            logger.info("Кнопка 'more' найдена и нажата")

        with allure.step("8. Нажатие кнопки 'select'"):
            logger.debug("Ищем кнопку 'select'")
            assert saved.clicks.safe_click(saved.SELECT_TV), "Кнопка 'select' не найдена"
            logger.info("Кнопка 'select' найдена и нажата")

        with allure.step("9. Выход с активности кнопки 'select' с помощью кнопки 'Done'"):
            logger.debug("Ищем кнопку 'Done'")
            assert saved.clicks.safe_click(saved.DONE_IV), "Кнопка 'Done' не найдена"
            logger.info("Кнопка 'Done' найдена и нажата")
            logger.debug("Проверяем, что мы на экране с предложением логина")
            assert saved.clicks.is_visible(saved.MESSAGE_TITLE_VIEW_TV), "Мы не на экране с предложением логина"
            logger.info("Находимся на экране с предложением логина")

        logger.info("=== Тест успешно завершен ===")
        saved.delete_array()
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