import pytest
import allure

@pytest.mark.tabs
@pytest.mark.smoke
@allure.description("""
**Проверка сохранения листа из вкладок (незалогированный аккаунт)**
""")
def test_save_tabs_as_list(pages, logger, skip_onboarding):
    """Тестирование сохранения листа из вкладок"""
    try:
        logger.info("=== Начало теста: Проверка сохранения листа из вкладок ===")
        explore = pages.explore

        with allure.step("1. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("2. Рандомно создаем первую вкладку через поиск"):
            assert explore.test_search_works(), f"Не удалось ввести текст в строку поиска"
            logger.info(f"Удалось ввести текст в строку поиска")
            assert explore.get_search_res_and_click_random()
            explore.clicks.safe_click(explore.CLOSE_GAME_BTN)

        with allure.step("3. Заходим в раздел вкладок"):
            assert explore.clicks.safe_click(explore.TABS_COUNT_TEXT_TV), "Мы не в разделе вкладок"
            logger.info("Мы в разделе вкладок")
            logger.info(f"Имеется {explore.get_tabs_count()} вкладка")

        with allure.step("4. Добавление вкладки с помощью плюса"):
            assert explore.clicks.safe_click(explore.NEW_TAB_BTN), "Не удалось нажать плюс"
            logger.info("Удалось нажать плюс")
            assert explore.clicks.safe_click(explore.TABS_COUNT_TEXT_TV)
            logger.info(f"Имеется {explore.get_tabs_count()} вкладки")

        with allure.step("5. Проверка сохранения листа из вкладок"):
            assert explore.clicks.safe_click(explore.MORE_OPTIONS_IV), "Не удалось нажать more"
            logger.info("Удалось нажать more")
            assert explore.clicks.safe_click(explore.SAVE_ALL_TABS_TV), "Не удалось нажать кнопку сохранения всех вкладок"
            logger.info("Удалось нажать кнопку сохранения всех вкладок")
            assert explore.save_list(), "Не удалось сохранить лист"
            logger.info("Удалось сохранить лист")

        with allure.step("6. Проверка, что лист сохранился на экране saved"):
            assert explore.clicks.safe_click(explore.MORE_OPTIONS_IV), "Не удалось нажать more"
            logger.info("Удалось нажать more")
            assert explore.clicks.safe_click(explore.EXPLORE_TV), "Кнопка explore не нажата"
            logger.info("Кнопка explore нажата")
            assert explore.clicks.safe_click(explore.SAVED_FL), "Не удалось найти кнопку saved"
            logger.info("Перешли на экран saved")
            assert explore.check_add_list(), "Сохранение сработало неверно"
            logger.info("Сохранение сработало верно")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.tabs
@pytest.mark.smoke
@allure.description("""
**Проверка удаления каждой вкладки по отдельности (незалогированный аккаунт)**
""")
def test_delete_all_tabs_one_by_one(pages, logger, skip_onboarding):
    """Тестирование удаления каждой вкладки по отдельности"""
    try:
        logger.info("=== Начало теста: Проверка удаления каждой вкладки по отдельности ===")
        explore = pages.explore

        with allure.step("1. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("2. Рандомно создаем первую вкладку через поиск"):
            assert explore.test_search_works(), f"Не удалось ввести текст в строку поиска"
            logger.info(f"Удалось ввести текст в строку поиска")
            assert explore.get_search_res_and_click_random()
            explore.clicks.safe_click(explore.CLOSE_GAME_BTN)

        with allure.step("3. Заходим в раздел вкладок"):
            assert explore.clicks.safe_click(explore.TABS_COUNT_TEXT_TV), "Мы не в разделе вкладок"
            logger.info("Мы в разделе вкладок")
            logger.info(f"Имеется {explore.get_tabs_count()} вкладка")

        with allure.step("4. Добавление вкладки с помощью плюса"):
            assert explore.clicks.safe_click(explore.NEW_TAB_BTN), "Не удалось нажать плюс"
            logger.info("Удалось нажать плюс")
            assert explore.clicks.safe_click(explore.TABS_COUNT_TEXT_TV)
            logger.info(f"Имеется {explore.get_tabs_count()} вкладки")

        with allure.step("5. Проверка удаления всех вкладок одна за одной"):
            assert explore.close_all_tabs()
            logger.info(f"Имеется {explore.get_tabs_count()} вкладок")
            if explore.get_tabs_count() == 0: logger.info("Все вкладки успешно удалены")
            else: logger.error("Удаление сработало неверно")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.tabs
@pytest.mark.smoke
@allure.description("""
**Проверка удаления всех вкладок в more (незалогированный аккаунт)**
""")
def test_delete_all_tabs_in_more(pages, logger, skip_onboarding):
    """Тестирование удаления всех вкладок в more"""
    try:
        logger.info("=== Начало теста: Проверка удаления всех вкладок в more ===")
        explore = pages.explore

        with allure.step("1. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("2. Рандомно создаем первую вкладку через поиск"):
            assert explore.test_search_works(), f"Не удалось ввести текст в строку поиска"
            logger.info(f"Удалось ввести текст в строку поиска")
            assert explore.get_search_res_and_click_random()
            explore.clicks.safe_click(explore.CLOSE_GAME_BTN)

        with allure.step("3. Заходим в раздел вкладок"):
            assert explore.clicks.safe_click(explore.TABS_COUNT_TEXT_TV), "Мы не в разделе вкладок"
            logger.info("Мы в разделе вкладок")
            logger.info(f"Имеется {explore.get_tabs_count()} вкладка")

        with allure.step("4. Добавление вкладки с помощью плюса"):
            assert explore.clicks.safe_click(explore.NEW_TAB_BTN), "Не удалось нажать плюс"
            logger.info("Удалось нажать плюс")
            assert explore.clicks.safe_click(explore.TABS_COUNT_TEXT_TV)
            logger.info(f"Имеется {explore.get_tabs_count()} вкладки")

        with allure.step("5. Проверка удаления всех вкладок в more"):
            assert explore.clicks.safe_click(explore.MORE_OPTIONS_IV), "Не удалось нажать more"
            logger.info("Удалось нажать more")
            assert explore.clicks.safe_click(explore.CLOSE_ALL_TABS_TV), "Не удалось нажать кнопку закрытия всех вкладок"
            logger.info("Удалось нажать кнопку закрытия всех вкладок")
            assert explore.clicks.safe_click(explore.NO_BUTTON2_BTN), "Не удалось найти иконку отмены удаления всехвкладок"
            logger.info("Кнопка отмены удаления вкладок работает")
            assert explore.clicks.safe_click(explore.MORE_OPTIONS_IV), "Не удалось нажать more"
            logger.info("Удалось нажать more")
            assert explore.clicks.safe_click(explore.CLOSE_ALL_TABS_TV), "Не удалось нажать кнопку закрытия всех вкладок"
            logger.info("Удалось нажать кнопку закрытия всех вкладок")
            assert explore.clicks.safe_click(explore.YES_BUTTON1_BTN), "Не удалось найти иконку подтверждения удаления всех вкладок"
            logger.info("Кнопка подтверждения удаления всех вкладок работает")
            logger.info("Проверка, что вкладок нет")
            logger.info(f"Имеется {explore.get_tabs_count()} вкладок")
            if explore.get_tabs_count() == 0: logger.info("Все вкладки успешно удалены")
            else: logger.error("Удаление сработало неверно")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.tabs
@pytest.mark.smoke
@allure.description("""
**Проверка кнопки explore в more (незалогированный аккаунт)**
""")
def test_press_explore_in_more(pages, logger, skip_onboarding):
    """Тестирование кнопки explore в more"""
    try:
        logger.info("=== Начало теста: Проверка кнопки explore в more ===")
        explore = pages.explore

        with allure.step("1. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("2. Рандомно создаем первую вкладку через поиск"):
            assert explore.test_search_works(), f"Не удалось ввести текст в строку поиска"
            logger.info(f"Удалось ввести текст в строку поиска")
            assert explore.get_search_res_and_click_random()
            explore.clicks.safe_click(explore.CLOSE_GAME_BTN)

        with allure.step("3. Заходим в раздел вкладок"):
            assert explore.clicks.safe_click(explore.TABS_COUNT_TEXT_TV), "Мы не в разделе вкладок"
            logger.info("Мы в разделе вкладок")
            logger.info(f"Имеется {explore.get_tabs_count()} вкладка")

        with allure.step("4. Проверка кнопки explore в more"):
            assert explore.clicks.safe_click(explore.MORE_OPTIONS_IV), "Не удалось нажать more"
            logger.info("Удалось нажать more")
            assert explore.clicks.safe_click(explore.EXPLORE_TV), "Кнопка explore не нажата"
            logger.info("Кнопка explore нажата")
            assert explore.clicks.is_visible(explore.SAVED_FL), "Кнопка explore в more работает неисправно"
            logger.info("Кнопка explore в more работает исправно")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.tabs
@pytest.mark.smoke
@allure.description("""
**Проверка добавления вкладки с помощью more (незалогированный аккаунт)**
""")
def test_add_tab_with_more(pages, logger, skip_onboarding):
    """Тестирование добавления вкладки с помощью more"""
    try:
        logger.info("=== Начало теста: Проверка добавления вкладки с помощью more ===")
        explore = pages.explore

        with allure.step("1. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("2. Рандомно создаем первую вкладку через поиск"):
            assert explore.test_search_works(), f"Не удалось ввести текст в строку поиска"
            logger.info(f"Удалось ввести текст в строку поиска")
            assert explore.get_search_res_and_click_random()
            explore.clicks.safe_click(explore.CLOSE_GAME_BTN)

        with allure.step("3. Заходим в раздел вкладок"):
            assert explore.clicks.safe_click(explore.TABS_COUNT_TEXT_TV), "Мы не в разделе вкладок"
            logger.info("Мы в разделе вкладок")
            logger.info(f"Имеется {explore.get_tabs_count()} вкладка")

        with allure.step("4. Добавление вкладки с помощью more"):
            assert explore.clicks.safe_click(explore.MORE_OPTIONS_IV), "Не удалось нажать more"
            logger.info("Удалось нажать more")
            assert explore.clicks.safe_click(explore.NEW_TAB_TV)
            assert explore.clicks.safe_click(explore.TABS_COUNT_TEXT_TV)
            logger.info(f"Имеется {explore.get_tabs_count()} вкладки")
            logger.info("Добавление через more работает исправно")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.tabs
@pytest.mark.smoke
@allure.description("""
**Проверка добавления вкладки с помощью иконки плюса (незалогированный аккаунт)**
""")
def test_add_tab_with_icon_plus(pages, logger, skip_onboarding):
    """Тестирование добавления вкладки с помощью иконки плюса"""
    try:
        logger.info("=== Начало теста: Проверка добавления вкладки с помощью иконки плюса ===")
        explore = pages.explore

        with allure.step("1. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("2. Рандомно создаем первую вкладку через поиск"):
            assert explore.test_search_works(), f"Не удалось ввести текст в строку поиска"
            logger.info(f"Удалось ввести текст в строку поиска")
            assert explore.get_search_res_and_click_random()
            explore.clicks.safe_click(explore.CLOSE_GAME_BTN)

        with allure.step("3. Заходим в раздел вкладок"):
            assert explore.clicks.safe_click(explore.TABS_COUNT_TEXT_TV), "Мы не в разделе вкладок"
            logger.info("Мы в разделе вкладок")
            logger.info(f"Имеется {explore.get_tabs_count()} вкладка")

        with allure.step("4. Добавление вкладки с помощью плюса"):
            assert explore.clicks.safe_click(explore.NEW_TAB_BTN), "Не удалось нажать плюс"
            logger.info("Удалось нажать плюс")
            assert explore.clicks.safe_click(explore.TABS_COUNT_TEXT_TV)
            logger.info(f"Имеется {explore.get_tabs_count()} вкладки")

        with allure.step("5. Попытка добавление еще одной вкладки с помощью плюса"):
            assert explore.clicks.safe_click(explore.NEW_TAB_BTN), "Не удалось добавить вкладку"
            logger.info("Добавили вкладку")
            assert explore.clicks.safe_click(explore.TABS_COUNT_TEXT_TV)
            logger.info(f"Имеется {explore.get_tabs_count()} вкладки")
            if explore.get_tabs_count() == 2: logger.info("Не удалось добавить еще одну вкладку т к такая уже существует")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.search
@pytest.mark.smoke
@allure.description("""
**Проверка работы фильтра истории поиска на экране search (незалогированный аккаунт)**
""")
def test_filter_of_search_on_search_false(pages, logger, skip_onboarding):
    """Тестирование работы фильтра истории поиска на экране search"""
    try:
        logger.info("=== Начало теста: Проверка работы фильтра истории поиска на экране search ===")
        explore = pages.explore

        with allure.step("1. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("2. Рандомно заполняем историю поиска"):
            k = explore.random_k()

            for i in range(k):
                assert explore.test_search_works(), f"Не удалось ввести {i+1}-й текст в строку поиска"
                logger.info(f"Удалось ввести {i+1}-й текст в строку поиска")
                assert explore.get_search_res_and_click_random()
                if i == 0:
                    explore.clicks.safe_click(explore.CLOSE_GAME_BTN)
                assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
                logger.info("Активность поиска найдена и нажата")

        with allure.step("3. Выходим из активности поиска"):
            for i in range(k+2):
                assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN), "Кнопка 'navigate_up' не найдена"
                logger.info("Кнопка 'navigate_up' найдена и нажата")
            logger.debug("Проверяем, что на экране 'explore'")
            assert explore.clicks.is_visible(explore.EXPLORE_FL), "Мы не на экране 'explore'"
            logger.info("Мы на экране 'explore'")

        with allure.step("4. Переход на экран search"):
            assert explore.clicks.safe_click(explore.SEARCH_FL), "Переход на экран search не выполнен"
            logger.info("Переход на экран search выполнен")

        with allure.step("5. Нажатие кнопки фильтра"):
            assert explore.clicks.safe_click(explore.FILTER_HISTORY_IV), "Кнопка 'Filter_history' не найдена"
            logger.info("Кнопка 'Filter_history' нажата")
            logger.debug("Проверяем, что мы на фильтрации листа")
            assert explore.clicks.is_visible(explore.DONE_IV), "Мы не на экране с фильтрацией листа"
            logger.info("Находимся на экране с фильтрацией листа")

        with allure.step("6. Поиск поля фильтрации для ввода текста"):
            logger.debug("Ищем поле для ввода текста 'search_src_text'")
            assert explore.clicks.is_visible(explore.SEARCH_SRC_TEXT_ACTV), "Поле 'search_src_text' не найдено"
            logger.info("Поле 'search_src_text' найдено")

        with allure.step("5. Ввод текста в поле фильтрации"):
            assert explore.test_filter_works_false(), "Поле не найдено"

        with allure.step("4. Проверка, что фильтр отработала корректно"):
            assert explore.clicks.is_visible(explore.SEARCH_EMPTY_TEXT_TV), "Фильтр сработал неверно"
            actual = []
            expected = []
            logger.debug(f"Actual: {actual}")
            logger.debug(f"Expected: {expected}")
            logger.info("Фильтр сработал верно")

        with allure.step("5. Выход с экрана фильтрации с помощью кнопки 'Done'"):
            logger.debug("Ищем кнопку 'Done'")
            assert explore.clicks.safe_click(explore.DONE_IV), "Кнопка 'Done' не найдена"
            logger.info("Кнопка 'Done' найдена и нажата")
            logger.debug("Проверяем, что мы на экране search")
            assert explore.clicks.is_visible(explore.CLEAR_HISTORY_IV), "Мы не на экране search"
            logger.info("Находимся на экране search")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.search
@pytest.mark.smoke
@allure.description("""
**Проверка работы фильтра истории поиска на экране search (незалогированный аккаунт)**
""")
def test_filter_of_search_on_search_true(pages, logger, skip_onboarding):
    """Тестирование работы фильтра истории поиска на экране search"""
    try:
        logger.info("=== Начало теста: Проверка работы фильтра истории поиска на экране search ===")
        explore = pages.explore
        with allure.step("1. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("2. Рандомно заполняем историю поиска"):
            k = explore.random_k()

            for i in range(k):
                assert explore.test_search_works(), f"Не удалось ввести {i+1}-й текст в строку поиска"
                logger.info(f"Удалось ввести {i+1}-й текст в строку поиска")
                assert explore.get_search_res_and_click_random()
                if i == 0:
                    explore.clicks.safe_click(explore.CLOSE_GAME_BTN)
                assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
                logger.info("Активность поиска найдена и нажата")

        with allure.step("3. Выходим из активности поиска"):
            for i in range(k+2):
                assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN), "Кнопка 'navigate_up' не найдена"
                logger.info("Кнопка 'navigate_up' найдена и нажата")
            logger.debug("Проверяем, что на экране 'explore'")
            assert explore.clicks.is_visible(explore.EXPLORE_FL), "Мы не на экране 'explore'"
            logger.info("Мы на экране 'explore'")

        with allure.step("4. Переход на экран search"):
            assert explore.clicks.safe_click(explore.SEARCH_FL), "Переход на экран search не выполнен"
            logger.info("Переход на экран search выполнен")

        with allure.step("5. Нажатие кнопки фильтра"):
            assert explore.clicks.safe_click(explore.FILTER_HISTORY_IV), "Кнопка 'Filter_history' не найдена"
            logger.info("Кнопка 'Filter_history' нажата")
            logger.debug("Проверяем, что мы на фильтрации листа")
            assert explore.clicks.is_visible(explore.DONE_IV), "Мы не на экране с фильтрацией листа"
            logger.info("Находимся на экране с фильтрацией листа")

        with allure.step("6. Поиск поля фильтрации для ввода текста"):
            logger.debug("Ищем поле для ввода текста 'search_src_text'")
            assert explore.clicks.is_visible(explore.SEARCH_SRC_TEXT_ACTV), "Поле 'search_src_text' не найдено"
            logger.info("Поле 'search_src_text' найдено")

        with allure.step("5. Ввод текста в поле фильтрации"):
            assert explore.test_filter_works_true(), "Поле не найдено"

        with allure.step("4. Проверка, что фильтр отработала корректно"):
            actual = explore.get_search_res()
            expected = [explore.name_article[explore.j_primary-1]]
            logger.debug(f"Actual: {actual}")
            logger.debug(f"Expected: {expected}")
            assert actual == expected, "Фильтр сработал неверно"
            logger.info("Фильтр сработал верно")

        with allure.step("5. Выход с экрана фильтрации с помощью кнопки 'Done'"):
            logger.debug("Ищем кнопку 'Done'")
            assert explore.clicks.safe_click(explore.DONE_IV), "Кнопка 'Done' не найдена"
            logger.info("Кнопка 'Done' найдена и нажата")
            logger.debug("Проверяем, что мы на экране search")
            assert explore.clicks.is_visible(explore.CLEAR_HISTORY_IV), "Мы не на экране search"
            logger.info("Находимся на экране search")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.search
@pytest.mark.smoke
@allure.description("""
**Проверка работы истории поиска на экране search (незалогированный аккаунт)**
""")
def test_history_of_search_on_search(pages, logger, skip_onboarding):
    """Тестирование работы истории поиска на экране search"""
    try:
        logger.info("=== Начало теста: Проверка работы истории поиска на экране search ===")
        explore = pages.explore

        with allure.step("1. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("2. Рандомно заполняем историю поиска"):
            k = explore.random_k()

            for i in range(k):
                assert explore.test_search_works(), f"Не удалось ввести {i+1}-й текст в строку поиска"
                logger.info(f"Удалось ввести {i+1}-й текст в строку поиска")
                assert explore.get_search_res_and_click_random()
                if i == 0:
                    explore.clicks.safe_click(explore.CLOSE_GAME_BTN)
                assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
                logger.info("Активность поиска найдена и нажата")

        with allure.step("3. Проверка, что в истории поиска сохранились запросы"):
            logger.debug(f"Сохранённые запросы: {explore.test_text}")
            assert explore.verify_all_test_text_visible()

        with allure.step("4. Выходим из активности поиска"):
            for i in range(k+2):
                assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN), "Кнопка 'navigate_up' не найдена"
                logger.info("Кнопка 'navigate_up' найдена и нажата")
            logger.debug("Проверяем, что на экране 'explore'")
            assert explore.clicks.is_visible(explore.EXPLORE_FL), "Мы не на экране 'explore'"
            logger.info("Мы на экране 'explore'")

        with allure.step("5. Переход на экран search"):
            assert explore.clicks.safe_click(explore.SEARCH_FL), "Переход на экран search не выполнен"
            logger.info("Переход на экран search выполнен")

        with allure.step("6. Проверка, что в истории поиска сохранились статьи"):
            logger.debug(f"Сохранённые запросы: {explore.name_article}")
            assert explore.verify_all_name_article_visible()

        with allure.step("7. Проверка работы очистки истории поиска на экране explore"):
            logger.debug("Ищем иконку удаления истории")
            assert explore.clicks.safe_click(explore.CLEAR_HISTORY_IV), "Не удалось найти иконку удаления истории"
            logger.info("Кнопка удаления истории найдена и нажата")
            assert explore.clicks.safe_click(explore.NO_BUTTON2_BTN), "Не удалось найти иконку отмены удаления истории"
            logger.info("Кнопка отмены удаления работает")
            assert explore.clicks.safe_click(explore.CLEAR_HISTORY_IV), "Не удалось найти иконку удаления истории"
            logger.info("Кнопка удаления истории найдена и нажата")
            assert explore.clicks.safe_click(explore.YES_BUTTON1_BTN), "Не удалось найти иконку подтверждения удаления истории"
            logger.info("Кнопка подтверждения удаления работает")
            logger.info("Проверка, что история очищена")
            assert explore.clicks.is_visible(explore.HISTORY_EMPTY_IV), "История не пуста"
            logger.info("История пуста")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.search
@pytest.mark.smoke
@allure.description("""
**Проверка работы истории поиска на экране explore (незалогированный аккаунт)**
""")
def test_history_of_search_on_explore(pages, logger, skip_onboarding):
    """Тестирование работы истории поиска на экране explore"""
    try:
        logger.info("=== Начало теста: Проверка работы истории поиска на экране explore ===")
        explore = pages.explore

        with allure.step("1. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("2. Проверка, что история поиска пуста"):
            logger.debug("Ищем иконку пустой истории")
            assert explore.clicks.safe_click(explore.SEARCH_EMPTY_IV), "История не пуста"
            logger.info("История пуста")

        with allure.step("3. Рандомно заполняем историю поиска"):
            k = explore.random_k()

            for i in range(k):
                assert explore.test_search_works(), f"Не удалось ввести {i+1}-й текст в строку поиска"
                logger.info(f"Удалось ввести {i+1}-й текст в строку поиска")
                assert explore.get_search_res_and_click_random()
                if i == 0:
                    explore.clicks.safe_click(explore.CLOSE_GAME_BTN)
                assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
                logger.info("Активность поиска найдена и нажата")

        with allure.step("4. Проверка, что в истории поиска сохранились запросы"):
            logger.debug(f"Сохранённые запросы: {explore.test_text}")
            assert explore.verify_all_test_text_visible()

        with allure.step("5. Проверка работы очистки истории поиска на экране explore"):
            logger.debug("Ищем иконку удаления истории")
            assert explore.clicks.safe_click(explore.CLEAR_HISTORY_IV), "Не удалось найти иконку удаления истории"
            logger.info("Кнопка удаления истории найдена и нажата")
            assert explore.clicks.safe_click(explore.NO_BUTTON2_BTN), "Не удалось найти иконку отмены удаления истории"
            logger.info("Кнопка отмены удаления работает")
            assert explore.clicks.safe_click(explore.CLEAR_HISTORY_IV), "Не удалось найти иконку удаления истории"
            logger.info("Кнопка удаления истории найдена и нажата")
            assert explore.clicks.safe_click(explore.YES_BUTTON1_BTN), "Не удалось найти иконку подтверждения удаления истории"
            logger.info("Кнопка подтверждения удаления работает")
            logger.info("Проверка, что история очищена")
            assert explore.clicks.is_visible(explore.SEARCH_EMPTY_IV), "История не пуста"
            logger.info("История пуста")

        with allure.step("6. Выходим из активности поиска"):
            for i in range(k+2):
                assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN), "Кнопка 'navigate_up' не найдена"
                logger.info("Кнопка 'navigate_up' найдена и нажата")
            logger.debug("Проверяем, что на экране 'explore'")
            assert explore.clicks.is_visible(explore.EXPLORE_FL), "Мы не на экране 'explore'"
            logger.info("Мы на экране 'explore'")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.search
@pytest.mark.smoke
@allure.description("""
**Проверка работы строки 'search' на экране explore (незалогированный аккаунт)**
""")
def test_search_on_explore(pages, logger, skip_onboarding):
    """Тестирование строки 'search'"""
    try:
        logger.info("=== Начало теста: Проверка работы строки 'search' ===")
        explore = pages.explore

        with allure.step("1. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("2. Проверка, что поиск возвращает статьи, начинающиеся на то, что мы вводим в строке поиска"):
            assert explore.test_search_works(), "Не удалось ввести текст в строку поиска"
            logger.info("Удалось ввести текст в строку поиска")
            assert explore.check_search_results_start_with_text(), "Не все результаты соответствуют поисковому запросу"
            logger.info("Все результаты соответствуют поисковому запросу")

        with allure.step("3. Выходим из активности поиска"):
            assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN), "Кнопка 'navigate_up' не найдена"
            logger.info("Кнопка 'navigate_up' найдена и нажата")
            logger.debug("Проверяем, что на экране 'explore'")
            assert explore.clicks.is_visible(explore.EXPLORE_FL), "Мы не на экране 'explore'"
            logger.info("Мы на экране 'explore'")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise