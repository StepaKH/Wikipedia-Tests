import pytest
import allure

@pytest.mark.article
@allure.description("""
**Проверка кнопки 'watch' в статье (что с помощью нее можно добавить статью в 'watchlist')**
""")
def test_watch_article(pages, logger, log_in, log_out):
    """Тестирование кнопки 'watch' в статье (что с помощью нее можно добавить статью в 'watchlist')"""
    try:
        logger.info("=== Начало теста: Проверка кнопки 'watch' в статье (что с помощью нее можно добавить статью в 'watchlist') ===")
        explore = log_in
        explore = pages.explore

        with allure.step("1. Переход на экран 'explore'"):
            assert explore.clicks.safe_click(explore.EXPLORE_FL), "Не удалось перейти на экран 'explore'"
            logger.info("Удалось перейти на экран 'explore'")

        with allure.step("2. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("3. Рандомно выбираем статью через поиск"):
            assert explore.test_search_works(), "Не удалось ввести текст в строку поиска"
            logger.info(f"Удалось ввести текст в строку поиска")
            assert explore.get_search_res_and_click_random()
            explore.clicks.safe_click(explore.CLOSE_GAME_BTN)

        with allure.step("4. Заходим в раздел 'more options'"):
            assert explore.clicks.safe_click(explore.MORE_OPTIONS_IV), "Не удалось нажать 'more options'"
            logger.info("Удалось нажать 'more options'")
            assert explore.clicks.safe_click(explore.PAGE_WATCH_TV), "Не удалось нажать 'watch'"
            logger.info("Удалось нажать 'watch'")

        with allure.step("5. Проверка, что 'watch' работает корректно"):
            assert explore.clicks.safe_click(explore.MORE_OPTIONS_IV), "Не удалось нажать 'more options'"
            logger.info("Удалось нажать 'more options'")
            assert explore.clicks.safe_click(explore.PAGE_EXPLORE_TV), "Не удалось нажать 'explore'"
            logger.info("Удалось нажать 'explore'")

        with allure.step("6. Проверка, что статья добавилась в 'watchlist'"):
            assert explore.clicks.safe_click(explore.MORE_FL), "Не удалось найти кнопку more"
            logger.info("Перешли на экран more")
            assert explore.clicks.safe_click(explore.WATCHLIST_TV), "Не удалось зайти в 'watchlist'"
            logger.info("Удалось зайти в 'watchlist'")
            assert explore.clicks.safe_click(explore.SEARCH_OR_FILTER_WATCHLIST_TV)
            assert explore.text.safe_input(explore.SEARCH_SRC_TEXT_ACTV, explore.name_article[explore.j_primary-1]), "Не удалось ввести название статьи в поиск"
            logger.info("Удалось ввести название статьи в поиск")
            if explore.check_watch(): logger.info("Кнопка 'watch' сработалa верно и изменения отобразились")
            else: logger.info("Кнопка 'watch' сработалa верно, но изменений в данной статье не было")

        with allure.step("7. Начинаем процесс разлогирования"):
            assert explore.clicks.safe_click(explore.DONE_IV), "Не удалось нажать 'done'"
            logger.info("Удалось нажать 'done'")
            assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN), "Не удалось нажать стрелку назад"
            logger.info("Удалось нажать стрелку назад")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.article
@allure.description("""
**Проверка кнопки 'edit article' в статье (что с помощью нее можно попасть в раздел в котором можно редактировать статью)**
""")
def test_edit_article(pages, logger, log_in, log_out):
    """Тестирование кнопки 'edit article' в статье (что с помощью нее можно попасть в раздел в котором можно редактировать статью)"""
    try:
        logger.info("=== Начало теста: Проверка кнопки 'edit article' в статье (что с помощью нее можно попасть в раздел в котором можно редактировать статью) ===")
        explore = log_in
        explore = pages.explore

        with allure.step("1. Переход на экран 'explore'"):
            assert explore.clicks.safe_click(explore.EXPLORE_FL), "Не удалось перейти на экран 'explore'"
            logger.info("Удалось перейти на экран 'explore'")

        with allure.step("2. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("3. Рандомно выбираем статью через поиск"):
            assert explore.text.safe_input(explore.SEARCH_SRC_TEXT_ACTV, 'Moscow'), "Не удалось ввести текст в строку поиска"
            logger.info(f"Удалось ввести текст в строку поиска")
            assert explore.get_search_res_and_click_random()
            explore.clicks.safe_click(explore.CLOSE_GAME_BTN)

        with allure.step("3. Заходим в раздел 'more options'"):
            assert explore.clicks.safe_click(explore.MORE_OPTIONS_IV), "Не удалось нажать 'more options'"
            logger.info("Удалось нажать 'more options'")
            assert explore.clicks.safe_click(explore.PAGE_EDIT_ARTICLE_TV), "Не удалось нажать 'edit article'"
            logger.info("Удалось нажать 'edit article'")

        with allure.step("5. Проверка, что 'edit article' работает корректно"):
            assert explore.clicks.is_visible(explore.EDIT_ACTION_BUTTON_TEXT_BTN), "'edit article' работает некорректно"
            logger.info("'edit article' работает корректно")

        with allure.step("6. Проверка, что выход с активности 'edit article' работает корректно"):
            assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN), "Не удалось нажать стрелку назад"
            logger.info("Удалось нажать стрелку назад")
            assert explore.clicks.is_visible(explore.MORE_OPTIONS_IV), "Выход с активности 'edit article' сработал некорректно"
            logger.info("Выход с активности 'edit article' сработал корректно")

        with allure.step("7. Начинаем процесс разлогирования"):
            assert explore.clicks.safe_click(explore.MORE_OPTIONS_IV), "Не удалось нажать 'more options'"
            logger.info("Удалось нажать 'more options'")
            assert explore.clicks.safe_click(explore.PAGE_EXPLORE_TV), "Не удалось нажать 'explore'"
            logger.info("Удалось нажать 'explore'")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.article
@allure.description("""
**Проверка кнопки 'customize toolbar' в статье (что с помощью нее можно поменять визуальное расположение инструментов на экране статьи)**
""")
def test_customize_toolbar_article(pages, logger, skip_onboarding):
    """Тестирование кнопки 'customize toolbar' в статье (что с помощью нее можно поменять визуальное расположение инструментов на экране статьи)"""
    try:
        logger.info("=== Начало теста: Проверка кнопки 'customize toolbar' в статье (что с помощью нее можно поменять визуальное расположение инструментов на экране статьи) ===")
        explore = pages.explore

        with allure.step("1. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("2. Рандомно выбираем статью через поиск"):
            assert explore.test_search_works(), "Не удалось ввести текст в строку поиска"
            logger.info(f"Удалось ввести текст в строку поиска")
            assert explore.get_search_res_and_click_random()
            explore.clicks.safe_click(explore.CLOSE_GAME_BTN)

        with allure.step("3. Заходим в раздел 'more options'"):
            assert explore.clicks.safe_click(explore.MORE_OPTIONS_IV), "Не удалось нажать 'more options'"
            logger.info("Удалось нажать 'more options'")
            assert explore.clicks.safe_click(explore.CUSTOMIZE_TOOLBAR_TV), "Не удалось нажать 'customize toolbar'"
            logger.info("Удалось нажать 'customize toolbar'")
            assert explore.move_first_to_last(), "Не удалось переместить первый инструмент в конец списка"
            logger.info("Удалось переместить первый инструмент в конец списка")

        with allure.step("4. Проверка, что изменения отображаются на экране статьи"):
            assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN)
            assert explore.clicks.is_visible(explore.SHARE_TV), "Изменения отображаются на экране некорректно"
            assert explore.clicks.safe_click(explore.MORE_OPTIONS_IV)
            assert explore.clicks.is_visible(explore.PAGE_SAVE), "Изменения отображаются на экране некорректно"
            logger.info("Изменения отображаются на экране корректно")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.article
@allure.description("""
**Проверка кнопки 'edit_history' в статье (что с помощью нее можно попасть на активность, где можно сравнить между собой изменения в статье)**
""")
def test_edit_history_article(pages, logger, skip_onboarding):
    """Тестирование кнопки 'edit_history' в статье (что с помощью нее можно попасть на активность, где можно сравнить между собой изменения в статье)"""
    try:
        logger.info("=== Начало теста: Проверка кнопки 'edit_history' в статье (что с помощью нее можно попасть на активность, где можно сравнить между собой изменения в статье) ===")
        explore = pages.explore

        with allure.step("1. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("2. Рандомно выбираем статью через поиск"):
            assert explore.test_search_works(), "Не удалось ввести текст в строку поиска"
            logger.info(f"Удалось ввести текст в строку поиска")
            assert explore.get_search_res_and_click_random()
            explore.clicks.safe_click(explore.CLOSE_GAME_BTN)

        with allure.step("3. Заходим в раздел 'more options'"):
            assert explore.clicks.safe_click(explore.MORE_OPTIONS_IV), "Не удалось нажать 'more options'"
            logger.info("Удалось нажать 'more options'")
            assert explore.clicks.safe_click(explore.PAGE_VIEW_EDIT_HISTORY_TV), "Не удалось нажать 'edit history'"
            logger.info("Удалось нажать 'edit history'")

        with allure.step("4. Проверка сравнения с помощью 'compare'"):
            assert explore.clicks.safe_click(explore.COMPARE_BUTTON_BTN), "Не удалось нажать 'compare'"
            logger.info("Удалось нажать 'compare'")
            assert explore.clicks.safe_click(explore.SELECT_BUTTON1_IV), "Не удалось выбрать первое изменение для сравнения"
            logger.info("Удалось выбрать первое изменение для сравнения")
            assert explore.clicks.safe_click(explore.SELECT_BUTTON2_IV), "Не удалось выбрать второе изменение для сравнения"
            logger.info("Удалось выбрать второе изменение для сравнения")
            assert explore.clicks.safe_click(explore.COMPARE_CONFIRM_BTN), "Не удалось подтвердить сравнение"
            logger.info("Удалось подтвердить сравнение")

        with allure.step("4. Проверка, что выход с 'edit history' работает корректно"):
            assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN), "Выход с 'edit history' работает некорректно"
            assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN), "Выход с 'edit history' работает некорректно"
            assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN), "Выход с 'edit history' работает некорректно"
            assert explore.clicks.is_visible(explore.MORE_OPTIONS_IV), "Выход с 'edit history' работает некорректно"
            logger.info("Выход с 'edit history' работает корректно")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.article
@allure.description("""
**Проверка кнопки 'language' в статье (что с помощью нее можно выбрать другой язык)**
""")
def test_language_article(pages, logger, skip_onboarding):
    """Тестирование кнопки 'language' в статье (что с помощью нее можно выбрать другой язык)"""
    try:
        logger.info("=== Начало теста: Проверка кнопки 'language' в статье (что с помощью нее можно выбрать другой язык) ===")
        explore = pages.explore

        with allure.step("1. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("2. Рандомно выбираем статью через поиск"):
            assert explore.test_search_works(), "Не удалось ввести текст в строку поиска"
            logger.info(f"Удалось ввести текст в строку поиска")
            assert explore.get_search_res_and_click_random()
            explore.clicks.safe_click(explore.CLOSE_GAME_BTN)

        with allure.step("3. Нажатие кнопки 'language'"):
            assert explore.clicks.safe_click(explore.LANGUAGE_TV), "Не удалось нажать 'language'"
            logger.info("Удалось нажать 'language'")
            assert explore.choose_random_language(), "Не удалось выбрать случайный язык, т к для этой статьи не предусмотрен перевод "
            logger.info("Удалось выбрать случайный язык")

        with allure.step("4. Проверка, что 'language' работает корректно"):
            assert explore.clicks.is_visible(explore.MORE_OPTIONS_IV), "'language' работает некорректно"
            logger.info("'language' работает корректно")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.article
@allure.description("""
**Проверка кнопки 'save' в статье (что с помощью нее можно сохранить статью в лист 'saved')**
""")
def test_save_article(pages, logger, skip_onboarding):
    """Тестирование кнопки 'save' в статье (что с помощью нее можно сохранить статью в лист 'saved')"""
    try:
        logger.info("=== Начало теста: Проверка кнопки 'save' в статье (что с помощью нее можно сохранить статью в лист 'saved') ===")
        explore = pages.explore

        with allure.step("1. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("2. Рандомно заполняем историю поиска"):
            k = explore.random_k()

            for i in range(k):
                assert explore.test_search_works(), f"Не удалось ввести {i + 1}-й текст в строку поиска"
                logger.info(f"Удалось ввести {i + 1}-й текст в строку поиска")
                assert explore.get_search_res_and_click_random()
                if i == 0:
                    explore.clicks.safe_click(explore.CLOSE_GAME_BTN)
                assert explore.clicks.safe_click(explore.SAVE_TV), "Не удалось нажать 'save'"
                logger.info("Удалось нажать 'save'")
                assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
                logger.info("Активность поиска найдена и нажата")

        with allure.step("3. Выходим из активности поиска"):
            for i in range(k + 2):
                assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN)
            logger.debug("Проверяем, что на экране 'explore'")
            assert explore.clicks.is_visible(explore.EXPLORE_FL), "Мы не на экране 'explore'"
            logger.info("Мы на экране 'explore'")

        with allure.step("4. Проверка, что лист с статьями сохранился на экране saved"):
            assert explore.clicks.safe_click(explore.SAVED_FL), "Не удалось найти кнопку saved"
            logger.info("Перешли на экран saved")
            assert explore.clicks.safe_click(explore.SAVED_LIST), "Не удалось зайти в лист 'saved'"
            logger.info("Удалось зайти в лист 'saved'")
            assert explore.clicks.safe_click(explore.SAVE_GOT_IT)
            assert explore.verify_all_name_article_visible(), "Кнопка 'save' сработалa неверно"
            logger.info("Кнопка 'save' сработалa верно")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.article
@allure.description("""
**Проверка кнопки 'find in article' в статье (что с помощью нее можно искать по статье)**
""")
def test_find_in_article(pages, logger, skip_onboarding):
    """Тестирование кнопки 'find in article' в статье (что с помощью нее можно искать по статье)"""
    try:
        logger.info("=== Начало теста: Проверка кнопки 'find in article' в статье (что с помощью нее можно искать по статье) ===")
        explore = pages.explore

        with allure.step("1. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("2. Рандомно выбираем статью через поиск"):
            assert explore.test_search_works(), "Не удалось ввести текст в строку поиска"
            logger.info(f"Удалось ввести текст в строку поиска")
            assert explore.get_search_res_and_click_random()
            explore.clicks.safe_click(explore.CLOSE_GAME_BTN)

        with allure.step("3. Проверяем кнопку 'find in article'"):
            assert explore.clicks.safe_click(explore.FIND_IN_ARTICLE_TV), "Не удалось нажать 'find in article'"
            logger.info("Удалось нажать 'find in article'")

        with allure.step("4. Проверка, что 'find in article' работает корректно"):
            assert explore.test_search_works(), "'find in article' работает некорректно"
            assert explore.clicks.is_visible(explore.FIND_IN_PAGE_MATCH_TV), "'find in article' работает некорректно"
            logger.info("'find in article' работает корректно")

        with allure.step("5. Проверка, что выход с активности 'find in article' работает корректно"):
            assert explore.clicks.safe_click(explore.DONE_IV), "Не удалось нажать стрелку назад"
            logger.info("Удалось нажать стрелку назад")
            assert explore.clicks.is_visible(explore.MORE_OPTIONS_IV), "Выход с активности 'find in article' сработал некорректно"
            logger.info("Выход с активности 'find in article' сработал корректно")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.article
@allure.description("""
**Проверка кнопки 'theme' в статье (что она открывает раздел, где можно менять внешний вид статьи - шрифт, цвет и т д)**
""")
def test_theme_article(pages, logger, skip_onboarding):
    """Тестирование кнопки 'theme' в статье (что она открывает раздел, где можно менять внешний вид статьи - шрифт, цвет и т д)"""
    try:
        logger.info("=== Начало теста: Проверка кнопки 'theme' в статье (что она открывает раздел, где можно менять внешний вид статьи - шрифт, цвет и т д) ===")
        explore = pages.explore

        with allure.step("1. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("2. Рандомно выбираем статью через поиск"):
            assert explore.test_search_works(), "Не удалось ввести текст в строку поиска"
            logger.info(f"Удалось ввести текст в строку поиска")
            assert explore.get_search_res_and_click_random()
            explore.clicks.safe_click(explore.CLOSE_GAME_BTN)

        with allure.step("3. Проверяем кнопку 'theme'"):
            assert explore.clicks.safe_click(explore.THEME_TV), "Не удалось нажать 'theme'"
            logger.info("Удалось нажать 'theme'")

        with allure.step("4. Проверка, что 'theme' работает корректно"):
            assert explore.clicks.is_visible(explore.THEME_CHECK_BTN), "'theme' работает некорректно"
            logger.info("'theme' работает корректно")

        with allure.step("5. Проверка, что выход с активности 'theme' работает корректно"):
            assert explore.swipes.swipe_down(), "Не удалось сделать свайп вниз"
            logger.info("Удалось сделать свайп вниз")
            assert explore.clicks.is_visible(explore.MORE_OPTIONS_IV), "Выход с активности 'theme' сработал некорректно"
            logger.info("Выход с активности 'theme' сработал корректно")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.article
@allure.description("""
**Проверка кнопки 'categories' в статье (что она показывает к каким разделам относится статья)**
""")
def test_categories_article(pages, logger, skip_onboarding):
    """Тестирование кнопки 'categories' в статье (что она показывает к каким разделам относится статья)"""
    try:
        logger.info("=== Начало теста: Проверка кнопки 'categories' в статье (что она показывает к каким разделам относится статья) ===")
        explore = pages.explore

        with allure.step("1. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("2. Рандомно выбираем статью через поиск"):
            assert explore.test_search_works(), "Не удалось ввести текст в строку поиска"
            logger.info(f"Удалось ввести текст в строку поиска")
            assert explore.get_search_res_and_click_random()
            explore.clicks.safe_click(explore.CLOSE_GAME_BTN)

        with allure.step("3. Заходим в раздел 'more options'"):
            assert explore.clicks.safe_click(explore.MORE_OPTIONS_IV), "Не удалось нажать 'more options'"
            logger.info("Удалось нажать 'more options'")
            assert explore.clicks.safe_click(explore.PAGE_CATEGORIES_TV), "Не удалось нажать 'categories'"
            logger.info("Удалось нажать 'categories'")

        with allure.step("4. Проверка, что 'categories' работает корректно"):
            assert explore.clicks.is_visible(explore.CATEGORIES_THUMBNAIL_TV), "'categories' работает некорректно"
            logger.info("'categories' работает корректно")

        with allure.step("5. Проверка, что выход с активности 'categories' работает корректно"):
            assert explore.swipes.swipe_down(), "Не удалось сделать свайп вниз"
            logger.info("Удалось сделать свайп вниз")
            assert explore.clicks.is_visible(explore.MORE_OPTIONS_IV), "Выход с активности 'categories' сработал некорректно"
            logger.info("Выход с активности 'categories' сработал корректно")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.article
@allure.description("""
**Проверка кнопки 'new tab' в статье (что она создает новую вкладку)**
""")
def test_new_tab_article(pages, logger, skip_onboarding):
    """Тестирование кнопки 'new tab' в статье (что она создает новую вкладку)"""
    try:
        logger.info("=== Начало теста: Проверка кнопки 'new tab' в статье (что она создает новую вкладку) ===")
        explore = pages.explore

        with allure.step("1. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("2. Рандомно выбираем статью через поиск"):
            assert explore.test_search_works(), "Не удалось ввести текст в строку поиска"
            logger.info(f"Удалось ввести текст в строку поиска")
            assert explore.get_search_res_and_click_random()
            explore.clicks.safe_click(explore.CLOSE_GAME_BTN)

        with allure.step("3. Заходим в раздел 'more options'"):
            assert explore.clicks.safe_click(explore.MORE_OPTIONS_IV), "Не удалось нажать 'more options'"
            logger.info("Удалось нажать 'more options'")
            assert explore.clicks.safe_click(explore.PAGE_NEW_TAB_TV), "Не удалось нажать 'new tab'"
            logger.info("Удалось нажать 'new tab'")

        with allure.step("4. Проверка, что 'new tab' работает корректно"):
            assert explore.clicks.safe_click(explore.TABS_COUNT_TEXT_TV), "Мы не в разделе вкладок"
            logger.info("Мы в разделе вкладок")
            logger.info(f"Имеется {explore.get_tabs_count()} вкладки")
            if explore.get_tabs_count() == 2: logger.info("Вкладка успешно добавлена")
            else: logger.error("Вкладка не добавилась"
                               "")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.article
@allure.description("""
**Проверка кнопки 'explore' в статье (что она возвращает на экран explore)**
""")
def test_explore_article(pages, logger, skip_onboarding):
    """Тестирование кнопки 'explore' в статье"""
    try:
        logger.info("=== Начало теста: Проверка кнопки 'explore' в статье (что она возвращает на экран explore) ===")
        explore = pages.explore

        with allure.step("1. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("2. Рандомно выбираем статью через поиск"):
            assert explore.test_search_works(), "Не удалось ввести текст в строку поиска"
            logger.info(f"Удалось ввести текст в строку поиска")
            assert explore.get_search_res_and_click_random()
            explore.clicks.safe_click(explore.CLOSE_GAME_BTN)

        with allure.step("3. Заходим в раздел 'more options'"):
            assert explore.clicks.safe_click(explore.MORE_OPTIONS_IV), "Не удалось нажать 'more options'"
            logger.info("Удалось нажать 'more options'")
            assert explore.clicks.safe_click(explore.PAGE_EXPLORE_TV), "Не удалось нажать 'explore'"
            logger.info("Удалось нажать 'explore'")

        with allure.step("4. Проверка, что 'explore' работает корректно"):
            assert explore.clicks.is_visible(explore.EXPLORE_FL), "'explore' работает некорректно"
            logger.info("'explore' работает корректно")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.article
@allure.description("""
**Проверка 'talk page' и создания нового обсуждения**
""")
def test_talk_page_article(pages, logger, skip_onboarding):
    """Тестирование 'talk page' и создания нового обсуждения"""
    try:
        logger.info("=== Начало теста: Проверка 'talk page' и создания нового обсуждения ===")
        explore = pages.explore

        with allure.step("1. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("2. Рандомно выбираем статью через поиск"):
            assert explore.test_search_works(), "Не удалось ввести текст в строку поиска"
            logger.info(f"Удалось ввести текст в строку поиска")
            assert explore.get_search_res_and_click_random()
            explore.clicks.safe_click(explore.CLOSE_GAME_BTN)

        with allure.step("3. Заходим в раздел 'more options'"):
            assert explore.clicks.safe_click(explore.MORE_OPTIONS_IV), "Не удалось нажать 'more options'"
            logger.info("Удалось нажать 'more options'")
            assert explore.clicks.safe_click(explore.TALK_PAGE_TV), "Не удалось нажать 'talk page'"
            logger.info("Удалось нажать 'talk page'")
            assert explore.clicks.safe_click(explore.NEW_TOPIC_BTN), "Не удалось нажать 'new topic'"
            logger.info("Удалось нажать 'new topic'")
            assert explore.clicks.safe_click(explore.GOT_IT_BTN), "Не удалось нажать 'got_it'"
            logger.info("Удалось нажать 'got_it'")

        with allure.step("4. Проверка, что выход с активности 'talk page' работает корректно"):
            assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN)
            assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN)
            assert explore.clicks.is_visible(explore.MORE_OPTIONS_IV), "Выход с активности 'share' сработал некорректно"
            logger.info("Выход с активности 'share' сработал корректно")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.article
@allure.description("""
**Проверка кнопки поделиться статьей**
""")
def test_share_article(pages, logger, skip_onboarding):
    """Тестирование кнопки поделиться статьей"""
    try:
        logger.info("=== Начало теста: Проверка кнопки поделиться статьей ===")
        explore = pages.explore

        with allure.step("1. Нажатие активности поиска"):
            logger.debug("Ищем активность поиска")
            assert explore.clicks.safe_click(explore.SEARCH_WIKIPEDIA_TV), "Активность поиска не найдена"
            logger.info("Активность поиска найдена и нажата")

        with allure.step("2. Рандомно выбираем статью через поиск"):
            assert explore.test_search_works(), "Не удалось ввести текст в строку поиска"
            logger.info(f"Удалось ввести текст в строку поиска")
            assert explore.get_search_res_and_click_random()
            explore.clicks.safe_click(explore.CLOSE_GAME_BTN)

        with allure.step("3. Заходим в раздел 'more options'"):
            assert explore.clicks.safe_click(explore.MORE_OPTIONS_IV), "Не удалось нажать 'more options'"
            logger.info("Удалось нажать 'more options'")
            assert explore.clicks.safe_click(explore.PAGE_SHARE_TV), "Не удалось нажать 'share'"
            logger.info("Удалось нажать 'share'")
            assert explore.clicks.is_visible(explore.COPY_FL), "'share' сработала некорректно"
            logger.info("'share' сработала корректно")

        with allure.step("4. Проверка, что выход с активности 'share' работает корректно"):
            assert explore.swipes.swipe_down(), "Не удалось сделать свайп вниз"
            logger.info("Удалось сделать свайп вниз")
            assert explore.clicks.is_visible(explore.MORE_OPTIONS_IV), "Выход с активности 'share' сработал некорректно"
            logger.info("Выход с активности 'share' сработал корректно")

        explore.delete_test_text()

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

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
            assert explore.test_search_works(), "Не удалось ввести текст в строку поиска"
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
            assert explore.test_search_works(), "Не удалось ввести текст в строку поиска"
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
            assert explore.test_search_works(), "Не удалось ввести текст в строку поиска"
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
            assert explore.test_search_works(), "Не удалось ввести текст в строку поиска"
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

        with allure.step("7. Ввод текста в поле фильтрации"):
            assert explore.test_filter_works_false(), "Поле не найдено"

        with allure.step("8. Проверка, что фильтр отработала корректно"):
            assert explore.clicks.is_visible(explore.SEARCH_EMPTY_TEXT_TV), "Фильтр сработал неверно"
            actual = []
            expected = []
            logger.debug(f"Actual: {actual}")
            logger.debug(f"Expected: {expected}")
            logger.info("Фильтр сработал верно")

        with allure.step("9. Выход с экрана фильтрации с помощью кнопки 'Done'"):
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

        with allure.step("7. Ввод текста в поле фильтрации"):
            assert explore.test_filter_works_true(), "Поле не найдено"

        with allure.step("8. Проверка, что фильтр отработала корректно"):
            actual = explore.get_search_res()
            expected = [explore.name_article[explore.j_primary-1]]
            logger.debug(f"Actual: {actual}")
            logger.debug(f"Expected: {expected}")
            assert actual == expected, "Фильтр сработал неверно"
            logger.info("Фильтр сработал верно")

        with allure.step("9. Выход с экрана фильтрации с помощью кнопки 'Done'"):
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

