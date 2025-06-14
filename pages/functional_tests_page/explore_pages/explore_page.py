import random
import string

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from pages.functional_tests_page.base.base_page import BasePage

class ExplorePage(BasePage):
    def __init__(self, driver, logger=None):
        super().__init__(driver, logger=logger)
        self.logger = logger

    # Protected Locators
    SEARCH_FL = (AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Search']")
    EXPLORE_FL = (AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Explore']")
    SAVED_FL = (AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Saved']")

    #for search in explore
    SEARCH_WIKIPEDIA_TV = (AppiumBy.XPATH, "//android.widget.TextView[@text='Search Wikipedia']")
    SEARCH_SRC_TEXT_ACTV = (AppiumBy.XPATH, "//android.widget.AutoCompleteTextView[@resource-id='org.wikipedia.alpha:id/search_src_text']")
    NAVIGATE_UP_BTN = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")
    CLEAR_HISTORY_IV = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Clear history']")
    NO_BUTTON2_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='android:id/button2']")
    YES_BUTTON1_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='android:id/button1']")
    SEARCH_HISTORY_ITEMS = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/history_item_title']")
    SEARCH_EMPTY_IV = (AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='org.wikipedia.alpha:id/search_empty_image']")
    CLOSE_GAME_BTN = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Close']")

    #for search in search
    HISTORY_EMPTY_IV = (AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='org.wikipedia.alpha:id/history_empty_image']")
    FILTER_HISTORY_IV = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Filter history']")
    DONE_IV = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Done']")
    SEARCH_EMPTY_TEXT_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/search_empty_text']")

    #for tabs
    TABS_COUNT_TEXT_TV = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/tabsCountText"]')
    NEW_TAB_BTN = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='New tab']")
    MORE_OPTIONS_IV = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='More options']")
    NEW_TAB_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/title' and @text='New tab']")
    SAVE_ALL_TABS_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/title' and @text='Save all tabs']")
    EXPLORE_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/title' and @text='Explore']")

    #for close tabs
    CLOSE_ALL_TABS_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/title' and @text='Close all tabs']")

    # for save new list
    TEXT_INPUT_ET = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='org.wikipedia.alpha:id/text_input']")
    SECONDARY_TEXT_INPUT_ET = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='org.wikipedia.alpha:id/secondary_text_input']")
    CANCEL_BUTTON2_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='android:id/button2']")
    OK_BUTTON1_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='android:id/button1']")

    #for share
    PAGE_SHARE_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/page_share']")
    COPY_FL = (AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Copy']/android.widget.ImageView")

    #for talk page
    TALK_PAGE_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/page_view_talk_page']")
    NEW_TOPIC_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='org.wikipedia.alpha:id/talkNewTopicButton']")
    GOT_IT_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='android:id/button1']")

    #for page explore
    PAGE_EXPLORE_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/page_explore']")

    #for new tab
    PAGE_NEW_TAB_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/page_new_tab']")

    #for theme
    THEME_TV = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='Theme']")
    THEME_CHECK_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='org.wikipedia.alpha:id/button_font_family_sans_serif']")

    #for categories
    PAGE_CATEGORIES_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/page_categories']")
    CATEGORIES_THUMBNAIL_TV = (AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='org.wikipedia.alpha:id/categories_thumbnail']")

    #for find in article
    FIND_IN_ARTICLE_TV = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='Find in article']")
    FIND_IN_PAGE_MATCH_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/find_in_page_match']")

    #for save
    SAVE_TV = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='Save']")
    SAVED_LIST = ( AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/item_title']")
    SAVE_GOT_IT = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='org.wikipedia.alpha:id/buttonView']")

    #for edit article
    PAGE_EDIT_ARTICLE_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/page_edit_article']")
    EDIT_ACTION_BUTTON_TEXT_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='org.wikipedia.alpha:id/edit_actionbar_button_text']")

    #for language
    LANGUAGE_TV = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='Language']")
    SEARCH_FOR_A_LANGUAGE_BTN = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Search for a language']")
    LANGUAGE_TITLES = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/localized_language_name"]')

    #for watch
    PAGE_WATCH_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/page_watch']")
    MORE_FL = (AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='More']")
    WATCHLIST_TV = (AppiumBy.XPATH, '//android.widget.TextView[@text="Watchlist"]')
    SEARCH_OR_FILTER_WATCHLIST_TV = (AppiumBy.XPATH, '//android.widget.TextView[@text="Search or filter watchlist"]')

    #for edit history
    PAGE_VIEW_EDIT_HISTORY_TV = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/page_view_edit_history"]')
    COMPARE_BUTTON_BTN = (AppiumBy.XPATH, '//android.widget.Button[@resource-id="org.wikipedia.alpha:id/compareButton"]')
    SELECT_BUTTON1_IV = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="org.wikipedia.alpha:id/selectButton"])[1]')
    SELECT_BUTTON2_IV = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="org.wikipedia.alpha:id/selectButton"])[2]')
    COMPARE_CONFIRM_BTN = (AppiumBy.XPATH, '//android.widget.Button[@resource-id="org.wikipedia.alpha:id/compareConfirmButton"]')

    #for customize toolbar
    CUSTOMIZE_TOOLBAR_TV = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/customize_toolbar"]')
    DRAG_ICONS = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Hold the drag icon to move the item"]')
    SHARE_TV = (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Share"]')
    PAGE_SAVE = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/page_save"]')

    # for customize toolbar
    OPEN_CUSTOMIZE_BTN = (AppiumBy.XPATH, '//android.widget.Button[@resource-id="org.wikipedia.alpha:id/view_announcement_action_positive"]')
    VIEW_CARD_HEADER_TITLE_TV = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/view_card_header_title"]')
    TODAY_ON_WIKIPEDIA_TV = ( AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/view_card_header_title" and @text="Today on Wikipedia"]')
    #MORE_OPTIONS_IV = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='More options']")
    SHOW_ALL_TV = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/title" and @text="Show all"]')
    CHECKBOX1_SWITCH = (AppiumBy.XPATH, '(//android.widget.Switch[@resource-id="org.wikipedia.alpha:id/feed_content_type_checkbox"])[1]')
    CHECKBOX2_SWITCH = (AppiumBy.XPATH, '(//android.widget.Switch[@resource-id="org.wikipedia.alpha:id/feed_content_type_checkbox"])[2]')
    CHECKBOX3_SWITCH = (AppiumBy.XPATH, '(//android.widget.Switch[@resource-id="org.wikipedia.alpha:id/feed_content_type_checkbox"])[3]')
    CHECKBOX4_SWITCH = (AppiumBy.XPATH, '(//android.widget.Switch[@resource-id="org.wikipedia.alpha:id/feed_content_type_checkbox"])[4]')
    CHECKBOX5_SWITCH = (AppiumBy.XPATH, '(//android.widget.Switch[@resource-id="org.wikipedia.alpha:id/feed_content_type_checkbox"])[5]')
    CHECKBOX7_SWITCH = (AppiumBy.XPATH, '(//android.widget.Switch[@resource-id="org.wikipedia.alpha:id/feed_content_type_checkbox"])[7]')
    CHECKBOX8_SWITCH = (AppiumBy.XPATH, '(//android.widget.Switch[@resource-id="org.wikipedia.alpha:id/feed_content_type_checkbox"])[8]')
    CHECKBOX9_SWITCH = (AppiumBy.XPATH, '(//android.widget.Switch[@resource-id="org.wikipedia.alpha:id/feed_content_type_checkbox"])[9]')
    CHECKBOX10_SWITCH = (AppiumBy.XPATH, '(//android.widget.Switch[@resource-id="org.wikipedia.alpha:id/feed_content_type_checkbox"])[10]')

    #for got_it
    CUSTOMIZE_GOT_IT_BTN = (AppiumBy.XPATH, '//android.widget.Button[@resource-id="org.wikipedia.alpha:id/view_announcement_action_negative"]')
    SNACKBAR_TEXT_TV = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/snackbar_text"]')

    #for hide all
    HIDE_ALL_TV = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/title" and @text="Hide all"]')
    CUSTOMIZE_BTN = (AppiumBy.XPATH, '//android.widget.Button[@resource-id="org.wikipedia.alpha:id/customize_button"]')

    #for switch and restore
    FEED_SWITCH = (AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="org.wikipedia.alpha:id/feed_content_type_drag_handle"]')
    RESTORE_DEFAULT_VIEW_TV = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/title" and @text="Restore default view"]')
    CUSTOMIZE_THE_FEED_TV = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/title" and @text="Customize the feed"]')

    def log(self, level, msg):
        if self.logger:
            getattr(self.logger, level)(msg)

    feed = {'Wikipedia games', 'Featured article', 'Top read', 'Places nearby', 'Picture of the day', 'In the news', 'On this day', 'Random article', 'Today on wikipedia'}
    test_text = {}
    name_article = {}
    i_primary = 1
    j_primary = 1

    def random_k(self):
        return random.randint(2, 5)

    def delete_test_text(self):
        self.test_text.clear()
        self.name_article.clear()
        self.i_primary = 1
        self.j_primary = 1

    def test_search_works(self):
        self.test_text[self.i_primary] = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 3)))
        self.i_primary = self.i_primary + 1

        self.log("debug", f"=== Попытка ввода текста '{self.test_text[self.i_primary-1]}' ===")

        try:
            self.log("debug", f"Ввод '{self.test_text[self.i_primary-1]}' в поле фильтрации")
            if not self.text.safe_input(self.SEARCH_SRC_TEXT_ACTV, self.test_text[self.i_primary-1]):
                self.log("warning", f"⚠️ Не удалось ввести '{self.test_text[self.i_primary-1]}' в поле фильтрации")
                return False
            else: self.log("debug", f"Текст '{self.test_text[self.i_primary-1]}' введен успешно")

            return True
        except Exception as e:
            self.log("error", f"❌ Критическая ошибка при вводе текста: {str(e)}")
            return False

    def get_search_res(self):
        """Возвращает названия всех статей в виде списка."""
        SEARCH_RES_XPATH = "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/page_list_item_title']"
        self.clicks.wait_for_element((AppiumBy.XPATH, SEARCH_RES_XPATH))
        elements = self.driver.find_elements(AppiumBy.XPATH, SEARCH_RES_XPATH)
        return [el.text.strip() for el in elements if el.text.strip()]

    def check_search_results_start_with_text(self):
        """
        Проверяет, что все результаты поиска начинаются с текста из self.test_text.
        Возвращает True, если все элементы соответствуют условию, иначе False.
        """
        search_results = self.get_search_res()
        if not search_results:
            self.log("warning", "⚠️ Список результатов поиска пуст")
            return False

        for result in search_results:
            if not result.lower().startswith(self.test_text[self.i_primary-1].lower()):
                self.log("error", f"❌ Результат '{result}' не начинается с '{self.test_text[self.i_primary-1]}'")
                return False

        self.log("debug", f"✓ Все результаты начинаются с '{self.test_text[self.i_primary-1]}'")
        return True

    def get_search_res_and_click_random(self):
        """
        Возвращает названия всех статей в виде списка
        и кликает на случайный элемент из результатов поиска.
        """
        SEARCH_RES_XPATH = "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/page_list_item_title']"

        # Ожидаем появления элементов и получаем их
        self.clicks.wait_for_element((AppiumBy.XPATH, SEARCH_RES_XPATH))
        elements = self.driver.find_elements(AppiumBy.XPATH, SEARCH_RES_XPATH)
        results = [el.text.strip() for el in elements if el.text.strip()]

        if not results:
            self.log("warning", "⚠️ Не найдено результатов поиска")
            return results

        # Выбираем случайный элемент
        random_element = random.choice(elements)
        random_title = random_element.text.strip()
        self.name_article[self.j_primary] = random_title
        self.j_primary = self.j_primary + 1

        # Кликаем на случайный элемент
        try:
            locator = (AppiumBy.XPATH,
                       f"//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/page_list_item_title' "
                       f"and @text='{random_title}']")
            self.clicks.safe_click(locator)
            self.log("info", f"✓ Успешно кликнули на случайный результат: '{random_title}'")
        except Exception as e:
            self.log("error", f"❌ Ошибка при клике на элемент '{random_title}': {str(e)}")

        return True

    def verify_all_test_text_visible(self):
        """
        Проверяет, что все элементы из test_text видны на экране.
        Возвращает True, если все элементы видны, False если хотя бы один не виден.
        """
        all_visible = True

        for text in self.test_text.values():
            try:
                locator = (AppiumBy.XPATH, f'//android.widget.TextView[@text="{text}"]')
                if not self.clicks.is_visible(locator):
                    self.logger.warning(f"Элемент с текстом '{text}' не виден на экране")
                    all_visible = False
                else:
                    self.logger.debug(f"Элемент с текстом '{text}' успешно найден")
            except Exception as e:
                self.logger.error(f"Ошибка при проверке элемента '{text}': {str(e)}")
                all_visible = False

        return all_visible

    def verify_all_name_article_visible(self):
        """
        Проверяет, что все элементы из name_article видны на экране.
        Возвращает True, если все элементы видны, False если хотя бы один не виден.
        """
        all_visible = True

        for text in self.name_article.values():
            try:
                locator = (AppiumBy.XPATH, f'//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/page_list_item_title" and @text="{text}"]')
                if not self.clicks.is_visible(locator):
                    self.logger.warning(f"Элемент с текстом '{text}' не виден на экране")
                    all_visible = False
                else:
                    self.logger.debug(f"Элемент с текстом '{text}' успешно найден")
            except Exception as e:
                self.logger.error(f"Ошибка при проверке элемента '{text}': {str(e)}")
                all_visible = False

        return all_visible

    def test_filter_works_true(self):
        try:
            self.log("debug", f"Ввод '{self.name_article[self.j_primary-1]}' в поле фильтрации")
            if not self.text.safe_input(self.SEARCH_SRC_TEXT_ACTV, self.name_article[self.j_primary-1]):
                self.log("warning", f"⚠️ Не удалось ввести '{self.name_article[self.j_primary-1]}' в поле фильтрации")
                return False
            else: self.log("debug", f"Текст '{self.name_article[self.j_primary-1]}' в поле фильтрации введен успешно")

            return True
        except Exception as e:
            self.log("error", f"❌ Критическая ошибка при вводе текста: {str(e)}")
            return False

    def test_filter_works_false(self):
        test = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(7, 10)))
        try:
            self.log("debug", f"Ввод '{test}' в поле фильтрации")
            if not self.text.safe_input(self.SEARCH_SRC_TEXT_ACTV, test):
                self.log("warning", f"⚠️ Не удалось ввести '{test}' в поле фильтрации")
                return False
            else: self.log("debug", f"Текст '{test}' в поле фильтрации введен успешно")

            return True
        except Exception as e:
            self.log("error", f"❌ Критическая ошибка при вводе текста: {str(e)}")
            return False

    def get_tabs_count(self):
        """
        Возвращает количество открытых вкладок.
        Локатор ищет элементы с id 'org.wikipedia.alpha:id/tabArticleTitle'.
        """
        TABS_XPATH = "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/tabArticleTitle']"
        try:
            # Исправленный вызов wait_for_element - передаем кортеж (By, locator)
            self.clicks.wait_for_element((AppiumBy.XPATH, TABS_XPATH))

            elements = self.driver.find_elements(AppiumBy.XPATH, TABS_XPATH)
            count = len([el for el in elements if el.text.strip()])

            self.log("info", f"Найдено вкладок: {count}")
            return count

        except Exception as e:
            self.log("error", f"Ошибка при подсчете вкладок: {str(e)}")
            return 0

    def close_all_tabs(self):
        """
        Закрывает все вкладки в обратном порядке (с конца).
        Возвращает количество успешно закрытых вкладок.
        """
        TAB_CLOSE_BTN_XPATH = "//android.widget.ImageView[@resource-id='org.wikipedia.alpha:id/tabCloseButton']"
        closed_count = 0

        try:
            # Находим все кнопки закрытия
            close_buttons = self.driver.find_elements(AppiumBy.XPATH, TAB_CLOSE_BTN_XPATH)
            self.log("debug", f"Найдено кнопок закрытия: {len(close_buttons)}")

            # Закрываем в обратном порядке
            for btn in reversed(close_buttons):
                try:
                    if btn.is_displayed():
                        btn.click()
                        closed_count += 1
                        self.log("debug", f"Закрыта вкладка #{closed_count} (с конца)")
                except Exception as e:
                    self.log("warning", f"Не удалось закрыть вкладку: {str(e)}")
                    continue

            self.log("info", f"Всего закрыто вкладок: {closed_count} (в обратном порядке)")
            return closed_count

        except Exception as e:
            self.log("error", f"Ошибка при закрытии вкладок: {str(e)}")
            return closed_count

    test_primary_text = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    test_secondary_text = ''.join(random.choice(string.ascii_lowercase) for _ in range(20))
    def save_list(self):
        try:
            self.log("debug", f"=== Попытка ввода текста '{self.test_primary_text}' ===")

            self.log("debug", f"Ввод '{self.test_primary_text}' в поле фильтрации")
            if not self.text.safe_input(self.TEXT_INPUT_ET, self.test_primary_text):
                self.log("warning", f"⚠️ Не удалось ввести '{self.test_primary_text}' в поле фильтрации")
                return False
            else:
                self.log("debug", f"Текст '{self.test_primary_text}' введен успешно")

            self.log("debug", f"=== Попытка ввода текста '{self.test_secondary_text}' ===")

            self.log("debug", f"Ввод '{self.test_secondary_text}' в поле фильтрации")
            if not self.text.safe_input(self.SECONDARY_TEXT_INPUT_ET, self.test_secondary_text):
                self.log("warning", f"⚠️ Не удалось ввести '{self.test_secondary_text}' в поле фильтрации")
                return False
            else:
                self.log("debug", f"Текст '{self.test_secondary_text}' введен успешно")
            self.clicks.safe_click(self.OK_BUTTON1_BTN)
            return True


        except Exception as e:
            self.log("error", f"❌ Критическая ошибка при вводе текста: {str(e)}")
            return False

    def check_add_list(self):

        try:
            self.log("debug", f"=== Попытка найти добавленный лист на экране 'saved' ===")
            TITLE_ACTIVITI_VG = (AppiumBy.XPATH, "(//android.view.ViewGroup[@resource-id='org.wikipedia.alpha:id/item_title_container'])")

            if not self.clicks.is_visible(TITLE_ACTIVITI_VG):
                self.log("warning", f"⚠️ Не удалось найти лист '{self.test_primary_text}' на экране 'saved'")
                return False
            else: self.log("debug", f"Заголовок листа '{self.test_primary_text}' найден успешно")

            DESCRIPTION_ACTIVITI_TV = (AppiumBy.XPATH, f"//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/item_description' and @text='{self.test_secondary_text}']")

            if not self.clicks.is_visible(DESCRIPTION_ACTIVITI_TV):
                self.log("warning", f"⚠️ Не удалось найти лист '{self.test_secondary_text}' на экране 'saved'")
                return False
            else:
                self.log("debug", f"Лист '{self.test_secondary_text}' найден успешно")

            return True


        except Exception as e:
            self.log("error", f"❌ Критическая ошибка при проврке текста: {str(e)}")
            return False

    def choose_random_language(self, max_scrolls=5, click_fact=True):
        """
        Выбор случайного языка из списка. Возвращает имя выбранного языка или None, если не удалось.
        """
        try:
            scrolls = random.randint(0, max_scrolls)
            self.log('info', f"🔁 Прокрутка вниз: {scrolls} раз")

            for _ in range(scrolls):
                self.swipes.swipe_up()

            self.driver.implicitly_wait(2)
            elements = self.driver.find_elements(*self.LANGUAGE_TITLES)

            if not elements:
                self.log('warning', "⚠️ Не найдено языков на экране.")
                return None

            chosen = random.choice(elements)
            language_name = chosen.text.strip()

            if not language_name:
                self.log('warning', "⚠️ Выбранный язык без текста.")
                return None

            if click_fact:
                chosen.click()

            self.log('info', f"✅ Язык выбран: {language_name}")
            language = (AppiumBy.XPATH,f"//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/localized_language_name' and @text='{language_name}']")
            return language

        except Exception as e:
            self.log('error', f"❌ Ошибка при выборе языка: {str(e)}")
            return None

    def check_watch(self):
        """
        Проверяет, что все элементы из name_article видны на экране.
        Возвращает True, если все элементы видны, False если хотя бы один не виден.
        """
        all_visible = True

        for text in self.name_article.values():
            try:
                locator = (AppiumBy.XPATH, f'//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/titleText" and @text="{text}"]')
                if not self.clicks.is_visible(locator):
                    self.logger.warning(f"Элемент с текстом '{text}' не виден на экране")
                    all_visible = False
                else:
                    self.logger.debug(f"Элемент с текстом '{text}' успешно найден")
            except Exception as e:
                self.logger.error(f"Ошибка при проверке элемента '{text}': {str(e)}")
                all_visible = False

        return all_visible

    def move_first_to_last(self):
        """
        Перемещает первый элемент в самый низ списка
        Возвращает:
            bool: True если перемещение успешно, False если произошла ошибка
        """
        try:
            self.log("debug", "Получаем текущий список элементов")

            # Получаем все drag-элементы
            drag_elements = self.driver.find_elements(*self.DRAG_ICONS)

            if len(drag_elements) < 2:
                self.log("warning", "⚠️ Недостаточно элементов для перемещения (нужно минимум 2)")
                return False

            # Определяем индексы
            index_from = 0  # Первый элемент
            index_to = len(drag_elements) - 1  # Последний элемент

            self.log("debug", f"🔄 Перетаскиваем элемент с позиции {index_from} на {index_to}")

            # Получаем элементы для перемещения
            source = drag_elements[index_from]
            target = drag_elements[index_to]

            # Выполняем перемещение
            self.driver.drag_and_drop(source, target)

            # Ожидаем обновления списка
            WebDriverWait(self.driver, 5).until(
                lambda d: len(self.driver.find_elements(*self.DRAG_ICONS)) == len(drag_elements)
            )

            self.log("info", "✅ Первый элемент успешно перемещен в конец списка")
            return True

        except Exception as e:
            self.log("error", f"❌ Неожиданная ошибка при перемещении элемента: {str(e)}")
            return False

    def verify_feed_order_wikipedia_games(self):
        """
        Проверяет, что карточки в ленте расположены в заданном порядке
        с учетом особого локатора для 'Today on Wikipedia'
        Возвращает:
            bool: True если порядок совпадает, False если нет
        """
        expected_order = [
            'Featured article',
            'Top read',
            'Places nearby',
            'Picture of the day',
            'In the news',
            'On this day',
            'Random article',
            'Today on Wikipedia'
        ]

        found_titles = []
        max_swipes = 15
        current_swipes = 0

        try:
            self.log("debug", "Начинаем проверку порядка карточек в ленте")

            while current_swipes < max_swipes and len(found_titles) < len(expected_order):
                # Проверяем обычные карточки
                elements = self.driver.find_elements(*self.VIEW_CARD_HEADER_TITLE_TV)
                current_titles = [el.text for el in elements if el.text]

                # Проверяем особую карточку "Today on Wikipedia"
                try:
                    today_element = self.driver.find_element(*self.TODAY_ON_WIKIPEDIA_TV)
                    today_text = today_element.text
                    if today_text not in current_titles:
                        current_titles.append(today_text)
                except NoSuchElementException:
                    pass

                # Добавляем новые уникальные заголовки
                for title in current_titles:
                    if title in expected_order and title not in found_titles:
                        found_titles.append(title)
                        self.log("debug", f"Найдена карточка: {title}")

                # Проверяем частичное соответствие порядка
                for i in range(len(found_titles)):
                    if found_titles[i] != expected_order[i]:
                        self.log("warning",
                                 f"Несоответствие порядка на позиции {i}: ожидалось {expected_order[i]}, найдено {found_titles[i]}")
                        return False

                # Если нашли все карточки - выходим
                if len(found_titles) == len(expected_order):
                    break

                # Свайпаем вверх
                self.swipes.swipe_up_for_customize()
                current_swipes += 1

            # Финальная проверка
            if found_titles == expected_order:
                self.log("info", "✅ Порядок карточек в ленте соответствует ожидаемому")
                return True
            else:
                missing = set(expected_order) - set(found_titles)
                self.log("warning",
                         f"⚠️ Порядок карточек не совпадает. Ожидалось: {expected_order}, найдено: {found_titles}. Отсутствуют: {missing}")
                return False

        except Exception as e:
            self.log("error", f"❌ Ошибка при проверке порядка карточек: {str(e)}")
            return False

    def verify_feed_order_featured_article(self):
        """
        Проверяет, что карточки в ленте расположены в заданном порядке
        с учетом особого локатора для 'Today on Wikipedia'
        Возвращает:
            bool: True если порядок совпадает, False если нет
        """
        expected_order = [
            'Wikipedia games',
            'Top read',
            'Places nearby',
            'Picture of the day',
            'In the news',
            'On this day',
            'Random article',
            'Today on Wikipedia'
        ]

        found_titles = []
        max_swipes = 15
        current_swipes = 0

        try:
            self.log("debug", "Начинаем проверку порядка карточек в ленте")

            while current_swipes < max_swipes and len(found_titles) < len(expected_order):
                # Проверяем обычные карточки
                elements = self.driver.find_elements(*self.VIEW_CARD_HEADER_TITLE_TV)
                current_titles = [el.text for el in elements if el.text]

                # Проверяем особую карточку "Today on Wikipedia"
                try:
                    today_element = self.driver.find_element(*self.TODAY_ON_WIKIPEDIA_TV)
                    today_text = today_element.text
                    if today_text not in current_titles:
                        current_titles.append(today_text)
                except NoSuchElementException:
                    pass

                # Добавляем новые уникальные заголовки
                for title in current_titles:
                    if title in expected_order and title not in found_titles:
                        found_titles.append(title)
                        self.log("debug", f"Найдена карточка: {title}")

                # Проверяем частичное соответствие порядка
                for i in range(len(found_titles)):
                    if found_titles[i] != expected_order[i]:
                        self.log("warning",
                                 f"Несоответствие порядка на позиции {i}: ожидалось {expected_order[i]}, найдено {found_titles[i]}")
                        return False

                # Если нашли все карточки - выходим
                if len(found_titles) == len(expected_order):
                    break

                # Свайпаем вверх
                self.swipes.swipe_up_for_customize()
                current_swipes += 1

            # Финальная проверка
            if found_titles == expected_order:
                self.log("info", "✅ Порядок карточек в ленте соответствует ожидаемому")
                return True
            else:
                missing = set(expected_order) - set(found_titles)
                self.log("warning",
                         f"⚠️ Порядок карточек не совпадает. Ожидалось: {expected_order}, найдено: {found_titles}. Отсутствуют: {missing}")
                return False

        except Exception as e:
            self.log("error", f"❌ Ошибка при проверке порядка карточек: {str(e)}")
            return False

    def verify_feed_order(self):
        """
        Проверяет, что карточки в ленте расположены в заданном порядке
        с учетом особого локатора для 'Today on Wikipedia'
        Возвращает:
            bool: True если порядок совпадает, False если нет
        """
        expected_order = [
            'Wikipedia games',
            'Featured article',
            'Top read',
            'Places nearby',
            'Picture of the day',
            'In the news',
            'On this day',
            'Random article',
            'Today on Wikipedia'
        ]

        found_titles = []
        max_swipes = 15
        current_swipes = 0

        try:
            self.log("debug", "Начинаем проверку порядка карточек в ленте")

            while current_swipes < max_swipes and len(found_titles) < len(expected_order):
                # Проверяем обычные карточки
                elements = self.driver.find_elements(*self.VIEW_CARD_HEADER_TITLE_TV)
                current_titles = [el.text for el in elements if el.text]

                # Проверяем особую карточку "Today on Wikipedia"
                try:
                    today_element = self.driver.find_element(*self.TODAY_ON_WIKIPEDIA_TV)
                    today_text = today_element.text
                    if today_text not in current_titles:
                        current_titles.append(today_text)
                except NoSuchElementException:
                    pass

                # Добавляем новые уникальные заголовки
                for title in current_titles:
                    if title in expected_order and title not in found_titles:
                        found_titles.append(title)
                        self.log("debug", f"Найдена карточка: {title}")

                # Проверяем частичное соответствие порядка
                for i in range(len(found_titles)):
                    if found_titles[i] != expected_order[i]:
                        self.log("warning",
                                 f"Несоответствие порядка на позиции {i}: ожидалось {expected_order[i]}, найдено {found_titles[i]}")
                        return False

                # Если нашли все карточки - выходим
                if len(found_titles) == len(expected_order):
                    break

                # Свайпаем вверх
                self.swipes.swipe_up_for_customize()
                current_swipes += 1

            # Финальная проверка
            if found_titles == expected_order:
                self.log("info", "✅ Порядок карточек в ленте соответствует ожидаемому")
                return True
            else:
                missing = set(expected_order) - set(found_titles)
                self.log("warning",
                         f"⚠️ Порядок карточек не совпадает. Ожидалось: {expected_order}, найдено: {found_titles}. Отсутствуют: {missing}")
                return False

        except Exception as e:
            self.log("error", f"❌ Ошибка при проверке порядка карточек: {str(e)}")
            return False

    def verify_feed_order_change(self):
        """
        Проверяет, что карточки в ленте расположены в заданном порядке
        с учетом особого локатора для 'Today on Wikipedia'
        Возвращает:
            bool: True если порядок совпадает, False если нет
        """
        expected_order = [
            'Featured article',
            'Top read',
            'Places nearby',
            'Picture of the day',
            'In the news',
            'On this day',
            'Random article',
            'Wikipedia games',
            'Today on Wikipedia'
        ]

        found_titles = []
        max_swipes = 15
        current_swipes = 0

        try:
            self.log("debug", "Начинаем проверку порядка карточек в ленте")

            while current_swipes < max_swipes and len(found_titles) < len(expected_order):
                # Проверяем обычные карточки
                self.clicks.is_visible(self.VIEW_CARD_HEADER_TITLE_TV)
                elements = self.driver.find_elements(*self.VIEW_CARD_HEADER_TITLE_TV)
                current_titles = [el.text for el in elements if el.text]

                # Проверяем особую карточку "Today on Wikipedia"
                try:
                    today_element = self.driver.find_element(*self.TODAY_ON_WIKIPEDIA_TV)
                    today_text = today_element.text
                    if today_text not in current_titles:
                        current_titles.append(today_text)
                except NoSuchElementException:
                    pass

                # Добавляем новые уникальные заголовки
                for title in current_titles:
                    if title in expected_order and title not in found_titles:
                        found_titles.append(title)
                        self.log("debug", f"Найдена карточка: {title}")

                # Проверяем частичное соответствие порядка
                for i in range(len(found_titles)):
                    if found_titles[i] != expected_order[i]:
                        self.log("warning",
                                 f"Несоответствие порядка на позиции {i}: ожидалось {expected_order[i]}, найдено {found_titles[i]}")
                        return False

                # Если нашли все карточки - выходим
                if len(found_titles) == len(expected_order):
                    break

                # Свайпаем вверх
                self.swipes.swipe_up_for_customize()
                current_swipes += 1

            # Финальная проверка
            if found_titles == expected_order:
                self.log("info", "✅ Порядок карточек в ленте соответствует ожидаемому")
                return True
            else:
                missing = set(expected_order) - set(found_titles)
                self.log("warning",
                         f"⚠️ Порядок карточек не совпадает. Ожидалось: {expected_order}, найдено: {found_titles}. Отсутствуют: {missing}")
                return False

        except Exception as e:
            self.log("error", f"❌ Ошибка при проверке порядка карточек: {str(e)}")
            return False

    def verify_feed_order_today_on_wikipedia(self):
        """
        Проверяет, что карточки в ленте расположены в заданном порядке
        с учетом особого локатора для 'Today on Wikipedia'
        Возвращает:
            bool: True если порядок совпадает, False если нет
        """
        expected_order = [
            'Wikipedia games',
            'Featured article',
            'Top read',
            'Places nearby',
            'Picture of the day',
            'In the news',
            'On this day',
            'Random article'
        ]

        found_titles = []
        max_swipes = 15
        current_swipes = 0

        try:
            self.log("debug", "Начинаем проверку порядка карточек в ленте")

            while current_swipes < max_swipes and len(found_titles) < len(expected_order):
                # Проверяем обычные карточки
                elements = self.driver.find_elements(*self.VIEW_CARD_HEADER_TITLE_TV)
                current_titles = [el.text for el in elements if el.text]

                # Проверяем особую карточку "Today on Wikipedia"
                try:
                    today_element = self.driver.find_element(*self.TODAY_ON_WIKIPEDIA_TV)
                    today_text = today_element.text
                    if today_text not in current_titles:
                        current_titles.append(today_text)
                except NoSuchElementException:
                    pass

                # Добавляем новые уникальные заголовки
                for title in current_titles:
                    if title in expected_order and title not in found_titles:
                        found_titles.append(title)
                        self.log("debug", f"Найдена карточка: {title}")

                # Проверяем частичное соответствие порядка
                for i in range(len(found_titles)):
                    if found_titles[i] != expected_order[i]:
                        self.log("warning",
                                 f"Несоответствие порядка на позиции {i}: ожидалось {expected_order[i]}, найдено {found_titles[i]}")
                        return False

                # Если нашли все карточки - выходим
                if len(found_titles) == len(expected_order):
                    break

                # Свайпаем вверх
                self.swipes.swipe_up_for_customize()
                current_swipes += 1

            # Финальная проверка
            if found_titles == expected_order:
                self.log("info", "✅ Порядок карточек в ленте соответствует ожидаемому")
                return True
            else:
                missing = set(expected_order) - set(found_titles)
                self.log("warning",
                         f"⚠️ Порядок карточек не совпадает. Ожидалось: {expected_order}, найдено: {found_titles}. Отсутствуют: {missing}")
                return False

        except Exception as e:
            self.log("error", f"❌ Ошибка при проверке порядка карточек: {str(e)}")
            return False

    def move_first_to_last_feed(self):
        """
        Перемещает первый элемент в самый низ списка
        Возвращает:
            bool: True если перемещение успешно, False если произошла ошибка
        """
        try:
            self.log("debug", "Получаем текущий список элементов")

            # Получаем все drag-элементы
            drag_elements = self.driver.find_elements(*self.FEED_SWITCH)

            if len(drag_elements) < 2:
                self.log("warning", "⚠️ Недостаточно элементов для перемещения (нужно минимум 2)")
                return False

            # Определяем индексы
            index_from = 0  # Первый элемент
            index_to = len(drag_elements) - 1  # Последний элемент

            self.log("debug", f"🔄 Перетаскиваем элемент с позиции {index_from} на {index_to}")

            # Получаем элементы для перемещения
            source = drag_elements[index_from]
            target = drag_elements[index_to]

            # Выполняем перемещение
            self.driver.drag_and_drop(source, target)

            # Ожидаем обновления списка
            WebDriverWait(self.driver, 5).until(
                lambda d: len(self.driver.find_elements(*self.FEED_SWITCH)) == len(drag_elements)
            )

            self.log("info", "✅ Первый элемент успешно перемещен в конец списка")
            return True

        except Exception as e:
            self.log("error", f"❌ Неожиданная ошибка при перемещении элемента: {str(e)}")
            return False

    def random_hide_feed_items(self):
        """
        Случайным образом скрывает элементы ленты используя соответствующие свитчи
        Возвращает:
            list: Список скрытых элементов (delete_order)
        """
        expected_order = [
            'Wikipedia games',
            'Featured article',
            'Top read',
            'Places nearby',
            'Picture of the day',
            'In the news',
            'On this day',
            'Random article',
        ]

        # Соответствие элементов и их свитчей
        switch_mapping = {
            'Wikipedia games': self.CHECKBOX1_SWITCH,
            'Featured article': self.CHECKBOX2_SWITCH,
            'Top read': self.CHECKBOX3_SWITCH,
            'Places nearby': self.CHECKBOX4_SWITCH,
            'Picture of the day': self.CHECKBOX5_SWITCH,
            'In the news': self.CHECKBOX7_SWITCH,
            'On this day': self.CHECKBOX8_SWITCH,
            'Random article': self.CHECKBOX9_SWITCH,
        }

        num_to_hide = random.randint(1, len(expected_order))
        delete_order = random.sample(expected_order, num_to_hide)

        try:
            self.log("debug", f"Скрываем элементы: {delete_order}")

            # Скрываем выбранные элементы
            for item in delete_order:
                switch_locator = switch_mapping[item]
                try:
                    # Находим свитч и кликаем по нему
                    switch = self.driver.find_element(*switch_locator)
                    switch.click()
                    self.log("debug", f"Скрыт элемент: {item}")

                except Exception as e:
                    self.log("warning", f"Не удалось скрыть {item}: {str(e)}")
                    continue

            self.log("info", f"✅ Скрыты элементы: {delete_order}")
            return delete_order

        except Exception as e:
            self.log("error", f"❌ Ошибка при скрытии элементов: {str(e)}")
            return []

    def verify_feed_order_with_hidden(self, hidden_items=None):
        """
        Проверяет порядок карточек в ленте, исключая скрытые элементы

        Параметры:
            hidden_items (list): Список скрытых карточек, которые нужно исключить из проверки

        Возвращает:
            bool: True если порядок совпадает, False если нет
        """
        full_expected_order = [
            'Wikipedia games',
            'Featured article',
            'Top read',
            'Places nearby',
            'Picture of the day',
            'In the news',
            'On this day',
            'Random article',
            'Today on Wikipedia'
        ]

        # Исключаем скрытые элементы из ожидаемого порядка
        expected_order = [item for item in full_expected_order
                          if hidden_items is None or item not in hidden_items]

        found_titles = []
        max_swipes = 15
        current_swipes = 0

        try:
            self.log("debug", f"Начинаем проверку порядка карточек. Скрытые элементы: {hidden_items}")
            self.log("debug", f"Ожидаемый порядок после исключения: {expected_order}")

            while current_swipes < max_swipes and len(found_titles) < len(expected_order):
                # Проверяем обычные карточки
                elements = self.driver.find_elements(*self.VIEW_CARD_HEADER_TITLE_TV)
                current_titles = [el.text for el in elements if el.text]

                # Проверяем особую карточку "Today on Wikipedia" (если не скрыта)
                if 'Today on Wikipedia' not in (hidden_items or []):
                    try:
                        today_element = self.driver.find_element(*self.TODAY_ON_WIKIPEDIA_TV)
                        today_text = today_element.text
                        if today_text not in current_titles:
                            current_titles.append(today_text)
                    except NoSuchElementException:
                        pass

                # Добавляем новые уникальные заголовки (исключая скрытые)
                for title in current_titles:
                    if (title in expected_order and
                            title not in found_titles and
                            title not in (hidden_items or [])):
                        found_titles.append(title)
                        self.log("debug", f"Найдена карточка: {title}")

                # Проверяем частичное соответствие порядка
                for i in range(len(found_titles)):
                    if found_titles[i] != expected_order[i]:
                        self.log("warning",
                                 f"Несоответствие порядка на позиции {i}: ожидалось {expected_order[i]}, найдено {found_titles[i]}")
                        return False

                # Если нашли все карточки - выходим
                if len(found_titles) == len(expected_order):
                    break

                # Свайпаем вверх
                self.swipes.swipe_up_for_customize()
                current_swipes += 1

            # Финальная проверка
            if found_titles == expected_order:
                self.log("info", "✅ Порядок карточек в ленте соответствует ожидаемому")
                return True
            else:
                missing = set(expected_order) - set(found_titles)
                self.log("warning",
                         f"⚠️ Порядок карточек не совпадает. Ожидалось: {expected_order}, найдено: {found_titles}. Отсутствуют: {missing}")
                return False

        except Exception as e:
            self.log("error", f"❌ Ошибка при проверке порядка карточек: {str(e)}")
            return False
