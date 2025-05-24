import random
import string
from appium.webdriver.common.appiumby import AppiumBy
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
    #CLEAR_HISTORY_IV = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Clear history']")
    #NO_BUTTON2_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='android:id/button2']")
    #YES_BUTTON1_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='android:id/button1']")
    #//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/page_list_item_title" and @text="GhGk-63"]
    FILTER_HISTORY_IV = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Filter history']")
    DONE_IV = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Done']")
    #SEARCH_SRC_TEXT_ACTV = (AppiumBy.XPATH, "//android.widget.AutoCompleteTextView[@resource-id='org.wikipedia.alpha:id/search_src_text']")
    #//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/page_list_item_title" and @text="FHM's 100 Sexiest Women (UK)"]
    SEARCH_EMPTY_TEXT_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/search_empty_text']")

    #for tabs
    TABS_COUNT_TEXT_TV = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/tabsCountText"]')
    NEW_TAB_BTN = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='New tab']")
    MORE_OPTIONS_IV = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='More options']")
    #//android.view.ViewGroup[@resource-id="org.wikipedia.alpha:id/tabContainer"]  [1,2,3...]
    NEW_TAB_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/title' and @text='New tab']")
    SAVE_ALL_TABS_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/title' and @text='Save all tabs']")
    EXPLORE_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/title' and @text='Explore']")

    #for close tabs
    CLOSE_ALL_TABS_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/title' and @text='Close all tabs']")
    #NO_BUTTON2_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='android:id/button2']")
    #YES_BUTTON1_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='android:id/button1']")
    #TAB_CLOSE_BTN_IV = (AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='org.wikipedia.alpha:id/tabCloseButton'])[1]")

    # for save new list
    TEXT_INPUT_ET = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='org.wikipedia.alpha:id/text_input']")
    SECONDARY_TEXT_INPUT_ET = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='org.wikipedia.alpha:id/secondary_text_input']")
    CANCEL_BUTTON2_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='android:id/button2']")
    OK_BUTTON1_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='android:id/button1']")


    def log(self, level, msg):
        if self.logger:
            getattr(self.logger, level)(msg)


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