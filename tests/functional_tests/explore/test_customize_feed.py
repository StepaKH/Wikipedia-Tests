import pytest
import allure

@pytest.mark.customize_feed
@allure.description("""
**Проверка кнопки 'got it' (что она скрывает карточку с кастомизацией)**
""")
def test_got_it_customize(pages, logger, skip_onboarding):
    """Тестирование кнопки 'got it' (что она скрывает карточку с кастомизацией)"""
    try:
        logger.info("=== Начало теста: Проверка кнопки 'got it' (что она скрывает карточку с кастомизацией) ===")
        explore = pages.explore

        with allure.step("1. Нажатие кнопки 'got it'"):
            logger.debug("Ищем кнопку 'got it'")
            assert explore.clicks.safe_click(explore.CUSTOMIZE_GOT_IT_BTN), "Кнопка 'got it' не найдена"
            logger.info("Кнопка 'got it' найдена и нажата")

        with allure.step("2. Проверка, что карточка с предложением кастомизации скрыта"):
            assert explore.clicks.is_visible(explore.SNACKBAR_TEXT_TV), "Карточка с предложением кастомизации не скрыта, кнопка 'got it' работает некорректно"
            logger.info("Карточка с предложением кастомизации скрыта, кнопка 'got it' работает корректно")

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.customize_feed
@allure.description("""
**Проверка кнопки 'customize' (что она перекидывает на активность с кастомизацией ленты)**
""")
def test_customize_customize(pages, logger, skip_onboarding):
    """Тестирование кнопки 'customize' (что она перекидывает на активность с кастомизацией ленты)"""
    try:
        logger.info("=== Начало теста: Проверка кнопки 'customize' (что она перекидывает на активность с кастомизацией ленты) ===")
        explore = pages.explore

        with allure.step("1. Нажатие кнопки 'customize'"):
            logger.debug("Ищем кнопку 'customize'")
            assert explore.clicks.safe_click(explore.OPEN_CUSTOMIZE_BTN), "Кнопка 'customize' не найдена"
            logger.info("Кнопка 'customize' найдена и нажата")

        with allure.step("2. Проверка, что открылся экран кастомизации"):
            assert explore.clicks.is_visible(explore.CHECKBOX1_SWITCH), "Экран кастомизации ленты не открылся, кнопка 'customize' работает некорректно"
            logger.info("Экран кастомизации ленты открылся, кнопка 'customize' работает корректно")

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.customize_feed
@allure.description("""
**Проверка кнопки 'hide all' (что она скрывает все карточки из ленты)**
""")
def test_hide_all_customize(pages, logger, skip_onboarding):
    """Тестирование кнопки 'hide all' (что она скрывает все карточки из ленты)"""
    try:
        logger.info("=== Начало теста: Проверка кнопки 'hide all' (что она скрывает все карточки из ленты) ===")
        explore = pages.explore

        with allure.step("1. Проверка, что в ленте есть карточки"):
            assert explore.clicks.is_visible(explore.VIEW_CARD_HEADER_TITLE_TV), "В ленте нет карточек"
            logger.info("В ленте есть карточки")

        with allure.step("2. Нажатие кнопки 'customize'"):
            logger.debug("Ищем кнопку 'customize'")
            assert explore.clicks.safe_click(explore.OPEN_CUSTOMIZE_BTN), "Кнопка 'customize' не найдена"
            logger.info("Кнопка 'customize' найдена и нажата")

        with allure.step("3. Проверка, что открылся экран кастомизации"):
            assert explore.clicks.is_visible(explore.CHECKBOX1_SWITCH), "Экран кастомизации ленты не открылся"
            logger.info("Экран кастомизации ленты открылся")

        with allure.step("4. Нажатие кнопки 'hide_all'"):
            logger.debug("Ищем кнопку 'more options'")
            assert explore.clicks.safe_click(explore.MORE_OPTIONS_IV), "Не удалось нажать 'more options'"
            logger.info("Удалось нажать 'more options'")
            logger.debug("Ищем кнопку 'hide all'")
            assert explore.clicks.safe_click(explore.HIDE_ALL_TV), "Не удалось нажать 'hide all'"
            logger.info("Удалось нажать 'hide all'")

        with allure.step("5. Проверка, что кнопка 'hide_all' сработала корректно"):
            logger.debug("Выходим из экрана кастомизации назад в ленту")
            assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN), "Не удалось нажать 'navigate up'"
            logger.info("Удалось нажать 'navigate up'")
            logger.debug("Ищем иконку пустой ленты")
            assert explore.clicks.is_visible(explore.CUSTOMIZE_BTN), "Лента не пуста, 'hide_all' сработала некорректно"
            logger.info("Лента пуста, 'hide_all' сработала корректно")

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.customize_feed
@allure.description("""
**Проверка кнопки 'show all' (что она возвращает карточки в ленту)**
""")
def test_show_all_customize(pages, logger, skip_onboarding):
    """Тестирование кнопки 'show all' (что она возвращает карточки в ленту)"""
    try:
        logger.info("=== Начало теста: Проверка кнопки 'show all' (что она возвращает карточки в ленту) ===")
        explore = pages.explore

        with allure.step("1. Нажатие кнопки 'customize'"):
            logger.debug("Ищем кнопку 'customize'")
            assert explore.clicks.safe_click(explore.OPEN_CUSTOMIZE_BTN), "Кнопка 'customize' не найдена"
            logger.info("Кнопка 'customize' найдена и нажата")

        with allure.step("2. Проверка, что открылся экран кастомизации"):
            assert explore.clicks.is_visible(explore.CHECKBOX1_SWITCH), "Экран кастомизации ленты не открылся"
            logger.info("Экран кастомизации ленты открылся")

        with allure.step("3. Нажатие кнопки 'hide_all'"):
            logger.debug("Ищем кнопку 'more options'")
            assert explore.clicks.safe_click(explore.MORE_OPTIONS_IV), "Не удалось нажать 'more options'"
            logger.info("Удалось нажать 'more options'")
            logger.debug("Ищем кнопку 'hide all'")
            assert explore.clicks.safe_click(explore.HIDE_ALL_TV), "Не удалось нажать 'hide all'"
            logger.info("Удалось нажать 'hide all'")

        with allure.step("4. Проверка, что лента пуста"):
            logger.debug("Выходим из экрана кастомизации назад в ленту")
            assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN), "Не удалось нажать 'navigate up'"
            logger.info("Удалось нажать 'navigate up'")
            logger.debug("Ищем иконку пустой ленты")
            assert explore.clicks.is_visible(explore.CUSTOMIZE_BTN), "Лента не пуста"
            logger.info("Лента пуста")

        with allure.step("5. Нажатие кнопки 'show_all'"):
            logger.debug("Ищем кнопку 'customize'")
            assert explore.clicks.safe_click(explore.CUSTOMIZE_BTN), "Не удалось нажать 'customize'"
            logger.info("Удалось нажать 'customize'")
            logger.debug("Ищем кнопку 'more options'")
            assert explore.clicks.safe_click(explore.MORE_OPTIONS_IV), "Не удалось нажать 'more options'"
            logger.info("Удалось нажать 'more options'")
            logger.debug("Ищем кнопку 'show_all'")
            assert explore.clicks.safe_click(explore.SHOW_ALL_TV), "Не удалось нажать 'show_all'"
            logger.info("Удалось нажать 'show_all'")

        with allure.step("6. Проверка, что в ленту вернулись все карточки"):
            logger.debug("Выходим из экрана кастомизации назад в ленту")
            assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN), "Не удалось нажать 'navigate up'"
            logger.info("Удалось нажать 'navigate up'")
            assert explore.clicks.wait_for_element(explore.VIEW_CARD_HEADER_TITLE_TV), "Не дождались первой карточки"
            logger.debug("Проверяем, что все карточки отображаются в ленте")
            assert explore.verify_feed_order(), "Не все карточки вернулись в ленту, 'show_all' сработало некорректно"
            logger.info("Все карточки вернулись в ленту, 'show_all' сработало корректно")

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.customize_feed
@allure.description("""
**Проверка, что можно поменять местами карточки на экране кастомизации и что они поменяются местами и в ленте**
""")
def test_switch_card_customize(pages, logger, skip_onboarding):
    """Тестирование, что можно поменять местами карточки на экране кастомизации и что они поменяются местами и в ленте"""
    try:
        logger.info("=== Начало теста: Проверка, что можно поменять местами карточки на экране кастомизации и что они поменяются местами и в ленте ===")
        explore = pages.explore

        with allure.step("1. Нажатие кнопки 'customize'"):
            logger.debug("Ищем кнопку 'customize'")
            assert explore.clicks.safe_click(explore.OPEN_CUSTOMIZE_BTN), "Кнопка 'customize' не найдена"
            logger.info("Кнопка 'customize' найдена и нажата")

        with allure.step("2. Проверка, что открылся экран кастомизации"):
            assert explore.clicks.is_visible(explore.CHECKBOX1_SWITCH), "Экран кастомизации ленты не открылся"
            logger.info("Экран кастомизации ленты открылся")

        with allure.step("3. Делаем первую карточку последней"):
            assert explore.move_first_to_last_feed(), "Не удалось переместить первую карточку в конец списка"
            logger.info("Удалось переместить первую карточку в конец списка")

        with allure.step("4. Проверка, что в ленте первая карточка тоже стала последней"):
            logger.debug("Выходим из экрана кастомизации назад в ленту")
            assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN), "Не удалось нажать 'navigate up'"
            logger.info("Удалось нажать 'navigate up'")
            assert explore.clicks.wait_for_element(explore.VIEW_CARD_HEADER_TITLE_TV), "Не дождались первой карточки"
            logger.debug("Проверяем, что все карточки отображаются в ленте в измененном порядке")
            assert explore.verify_feed_order_change(), "Порядок карточек в ленте не изменился"
            logger.info("Порядок карточек в ленте изменился")

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.customize_feed
@allure.description("""
**Проверка, что можно поменять местами карточки на экране кастомизации, а потом с помощью кнопки 'restore' вернуть порядок к изначальному**
""")
def test_restore_customize(pages, logger, skip_onboarding):
    """Тестирование, что можно поменять местами карточки на экране кастомизации, а потом с помощью кнопки 'restore' вернуть порядок к изначальному"""
    try:
        logger.info("=== Начало теста: Проверка, что можно поменять местами карточки на экране кастомизации, а потом с помощью кнопки 'restore' вернуть порядок к изначальному ===")
        explore = pages.explore

        with allure.step("1. Нажатие кнопки 'customize'"):
            logger.debug("Ищем кнопку 'customize'")
            assert explore.clicks.safe_click(explore.OPEN_CUSTOMIZE_BTN), "Кнопка 'customize' не найдена"
            logger.info("Кнопка 'customize' найдена и нажата")

        with allure.step("2. Проверка, что открылся экран кастомизации"):
            assert explore.clicks.is_visible(explore.CHECKBOX1_SWITCH), "Экран кастомизации ленты не открылся"
            logger.info("Экран кастомизации ленты открылся")

        with allure.step("3. Делаем первую карточку последней"):
            assert explore.move_first_to_last_feed(), "Не удалось переместить первую карточку в конец списка"
            logger.info("Удалось переместить первую карточку в конец списка")

        with allure.step("4. Проверка, что в ленте первая карточка тоже стала последней"):
            logger.debug("Выходим из экрана кастомизации назад в ленту")
            assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN), "Не удалось нажать 'navigate up'"
            logger.info("Удалось нажать 'navigate up'")
            logger.debug("Проверяем, что все карточки отображаются в ленте в измененном порядке")
            assert explore.verify_feed_order_change(), "Порядок карточек в ленте не изменился"
            logger.info("Порядок карточек в ленте изменился")

        with allure.step("5. Проверка, что можно вернуть все назад с помощью кнопки 'restore'"):
            logger.debug("Ищем кнопку 'more options'")
            assert explore.clicks.safe_click(explore.MORE_OPTIONS_IV), "Не удалось нажать 'more options'"
            logger.info("Удалось нажать 'more options'")
            logger.debug("Ищем кнопку 'customize the feed'")
            assert explore.clicks.safe_click(explore.CUSTOMIZE_THE_FEED_TV), "Не удалось нажать 'customize the feed'"
            logger.info("Удалось нажать 'customize the feed'")
            logger.debug("Ищем кнопку 'more options'")
            assert explore.clicks.safe_click(explore.MORE_OPTIONS_IV), "Не удалось нажать 'more options'"
            logger.info("Удалось нажать 'more options'")
            logger.debug("Ищем кнопку 'restore'")
            assert explore.clicks.safe_click(explore.RESTORE_DEFAULT_VIEW_TV), "Не удалось нажать 'restore'"
            logger.info("Удалось нажать 'restore'")

        with allure.step("6. Проверка, что 'restore' сработла корректно"):
            logger.debug("Выходим из экрана кастомизации назад в ленту")
            assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN), "Не удалось нажать 'navigate up'"
            logger.info("Удалось нажать 'navigate up'")
            assert explore.clicks.wait_for_element(explore.VIEW_CARD_HEADER_TITLE_TV), "Не дождались первой карточки"
            logger.debug("Проверяем, что все карточки отображаются в ленте в базовом порядке")
            assert explore.verify_feed_order(), "Порядок карточек в ленте не базовый, 'restore' сработала некорректно"
            logger.info("Порядок карточек в ленте базовый, 'restore' сработала корректно")

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.customize_feed
@allure.description("""
**Проверка свитча для 'wikipedia_games' (что он скрывает эту карточку из ленты)**
""")
def test_hide_wikipedia_games_customize(pages, logger, skip_onboarding):
    """Тестирование свитча для 'wikipedia_games' (что он скрывает эту карточку из ленты)"""
    try:
        logger.info("=== Начало теста: Проверка свитча для 'wikipedia_games' (что он скрывает эту карточку из ленты) ===")
        explore = pages.explore

        with allure.step("1. Нажатие кнопки 'customize'"):
            logger.debug("Ищем кнопку 'customize'")
            assert explore.clicks.safe_click(explore.OPEN_CUSTOMIZE_BTN), "Кнопка 'customize' не найдена"
            logger.info("Кнопка 'customize' найдена и нажата")

        with allure.step("2. Проверка, что открылся экран кастомизации"):
            assert explore.clicks.is_visible(explore.CHECKBOX1_SWITCH), "Экран кастомизации ленты не открылся, кнопка 'customize' работает некорректно"
            logger.info("Экран кастомизации ленты открылся, кнопка 'customize' работает корректно")

        with allure.step("3. Скрытие карточки 'wikipedia_games' с помощью свитча"):
            logger.debug("Ищем свитч")
            assert explore.clicks.safe_click(explore.CHECKBOX1_SWITCH), "Свитч не найден"
            logger.info("Свитч найден и нажат")

        with allure.step("4. Проверка, что свитч сработал корректно"):
            logger.debug("Выходим из экрана кастомизации назад в ленту")
            assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN), "Не удалось нажать 'navigate up'"
            logger.info("Удалось нажать 'navigate up'")
            assert explore.clicks.wait_for_element(explore.VIEW_CARD_HEADER_TITLE_TV), "Не дождались первой карточки"
            logger.debug("Проверяем, что все карточки отображаются в ленте в базовом порядке без 'wikipedia_games'")
            assert explore.verify_feed_order_wikipedia_games(), "Порядок карточек в ленте не соответствует ожидаемому, свитч сработал некорректно"
            logger.info("Порядок карточек в ленте соответствует ожидаемому, свитч сработал корректно")

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.customize_feed
@allure.description("""
**Проверка свитча для 'featured_article' (что он скрывает эту карточку из ленты)**
""")
def test_hide_featured_article_customize(pages, logger, skip_onboarding):
    """Тестирование свитча для 'wikipedia_games' (что он скрывает эту карточку из ленты)"""
    try:
        logger.info("=== Начало теста: Проверка свитча для 'featured_article' (что он скрывает эту карточку из ленты) ===")
        explore = pages.explore

        with allure.step("1. Нажатие кнопки 'customize'"):
            logger.debug("Ищем кнопку 'customize'")
            assert explore.clicks.safe_click(explore.OPEN_CUSTOMIZE_BTN), "Кнопка 'customize' не найдена"
            logger.info("Кнопка 'customize' найдена и нажата")

        with allure.step("2. Проверка, что открылся экран кастомизации"):
            assert explore.clicks.is_visible(explore.CHECKBOX1_SWITCH), "Экран кастомизации ленты не открылся, кнопка 'customize' работает некорректно"
            logger.info("Экран кастомизации ленты открылся, кнопка 'customize' работает корректно")

        with allure.step("3. Скрытие карточки 'featured_article' с помощью свитча"):
            logger.debug("Ищем свитч")
            assert explore.clicks.safe_click(explore.CHECKBOX2_SWITCH), "Свитч не найден"
            logger.info("Свитч найден и нажат")

        with allure.step("4. Проверка, что свитч сработал корректно"):
            logger.debug("Выходим из экрана кастомизации назад в ленту")
            assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN), "Не удалось нажать 'navigate up'"
            logger.info("Удалось нажать 'navigate up'")
            assert explore.clicks.wait_for_element(explore.VIEW_CARD_HEADER_TITLE_TV), "Не дождались первой карточки"
            logger.debug("Проверяем, что все карточки отображаются в ленте в базовом порядке без 'featured_article'")
            assert explore.verify_feed_order_featured_article(), "Порядок карточек в ленте не соответствует ожидаемому, свитч сработал некорректно"
            logger.info("Порядок карточек в ленте соответствует ожидаемому, свитч сработал корректно")

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.customize_feed
@allure.description("""
**Проверка свитча для 'today_on_wikipedia' (что он скрывает эту карточку из ленты)**
""")
def test_today_on_wikipedia_customize(pages, logger, skip_onboarding):
    """Тестирование свитча для 'today_on_wikipedia' (что он скрывает эту карточку из ленты)"""
    try:
        logger.info("=== Начало теста: Проверка свитча для 'today_on_wikipedia' (что он скрывает эту карточку из ленты) ===")
        explore = pages.explore

        with allure.step("1. Нажатие кнопки 'customize'"):
            logger.debug("Ищем кнопку 'customize'")
            assert explore.clicks.safe_click(explore.OPEN_CUSTOMIZE_BTN), "Кнопка 'customize' не найдена"
            logger.info("Кнопка 'customize' найдена и нажата")

        with allure.step("2. Проверка, что открылся экран кастомизации"):
            assert explore.clicks.is_visible(explore.CHECKBOX1_SWITCH), "Экран кастомизации ленты не открылся, кнопка 'customize' работает некорректно"
            logger.info("Экран кастомизации ленты открылся, кнопка 'customize' работает корректно")

        with allure.step("3. Скрытие карточки 'today_on_wikipedia' с помощью свитча"):
            explore.swipes.swipe_up_for_customize()
            logger.debug("Ищем свитч")
            assert explore.clicks.safe_click(explore.CHECKBOX10_SWITCH), "Свитч не найден"
            logger.info("Свитч найден и нажат")

        with allure.step("4. Проверка, что свитч сработал корректно"):
            logger.debug("Выходим из экрана кастомизации назад в ленту")
            assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN), "Не удалось нажать 'navigate up'"
            logger.info("Удалось нажать 'navigate up'")
            assert explore.clicks.wait_for_element(explore.VIEW_CARD_HEADER_TITLE_TV), "Не дождались первой карточки"
            logger.debug("Проверяем, что все карточки отображаются в ленте в базовом порядке без 'today_on_wikipedia'")
            assert explore.verify_feed_order_today_on_wikipedia(), "Порядок карточек в ленте не соответствует ожидаемому, свитч сработал некорректно"
            logger.info("Порядок карточек в ленте соответствует ожидаемому, свитч сработал корректно")

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.customize_random
@allure.description("""
**Проверка, что можно скрыть рандомное количество рандомных карточек и в ленте все отобразится верно**
""")
def test_random_customize(pages, logger, skip_onboarding):
    """Тестирование, что можно скрыть рандомное количество рандомных карточек и в ленте все отобразится верно"""
    try:
        logger.info("=== Начало теста: Проверка, что можно скрыть рандомное количество рандомных карточек и в ленте все отобразится верно ===")
        explore = pages.explore

        with allure.step("1. Нажатие кнопки 'customize'"):
            logger.debug("Ищем кнопку 'customize'")
            assert explore.clicks.safe_click(explore.OPEN_CUSTOMIZE_BTN), "Кнопка 'customize' не найдена"
            logger.info("Кнопка 'customize' найдена и нажата")

        with allure.step("2. Проверка, что открылся экран кастомизации"):
            assert explore.clicks.is_visible(explore.CHECKBOX1_SWITCH), "Экран кастомизации ленты не открылся, кнопка 'customize' работает некорректно"
            logger.info("Экран кастомизации ленты открылся, кнопка 'customize' работает корректно")

        with allure.step("3. Скрытие рандомного количества рандомных карточек с помощью свитча"):
            hidden = explore.random_hide_feed_items()

        with allure.step("4. Проверка, что свитчи сработали корректно"):
            logger.debug("Выходим из экрана кастомизации назад в ленту")
            assert explore.clicks.safe_click(explore.NAVIGATE_UP_BTN), "Не удалось нажать 'navigate up'"
            logger.info("Удалось нажать 'navigate up'")
            assert explore.clicks.wait_for_element(explore.VIEW_CARD_HEADER_TITLE_TV), "Не дождались первой карточки"
            logger.debug("Проверяем, что все карточки отображаются в ленте в базовом порядке без 'today_on_wikipedia'")
            assert explore.verify_feed_order_with_hidden(hidden_items=hidden), "Порядок карточек в ленте не соответствует ожидаемому, свитчи сработали некорректно"
            logger.info("Порядок карточек в ленте соответствует ожидаемому, свитч сработали корректно")

        logger.info("=== Тест успешно завершен ===")
    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise