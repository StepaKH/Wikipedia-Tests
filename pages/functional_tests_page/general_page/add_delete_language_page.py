from appium.webdriver.common.appiumby import AppiumBy
from pages.functional_tests_page.base.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
import random

class LanguageActions(BasePage):
    def __init__(self, driver, logger=None):
        super().__init__(driver, logger=logger)
        self.logger = logger

    # Кнопка добавления языка
    ADD_LANGUAGE_TITLE = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/wiki_language_title" and @text="Add language"]')
    # Поле поиска
    SEARCH_FIELD = (AppiumBy.ID, "org.wikipedia.alpha:id/menu_search_language")
    # Поле вставки текста
    INPUT_TEXT_FIELD = (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")
    # Языки в списке
    LANGUAGE_TITLES = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/localized_language_name"]')
    # Иконка для drag-and-drop
    DRAG_ICONS = (AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="org.wikipedia.alpha:id/wiki_language_drag_handle"]')
    # Кнопка назад
    BACK_BTN = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")
    # Меню (три точки)
    MENU_BTN = (AppiumBy.ACCESSIBILITY_ID, "More options")
    # Кнопка "Remove language"
    REMOVE_LANGUAGE_BTN = (AppiumBy.ID, "org.wikipedia.alpha:id/content")
    FIND_LANGUAGE_TITLE = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/wiki_language_title"]')
    DELETE_BUTTOM = (AppiumBy.ACCESSIBILITY_ID, "Delete selected items")
    OK_DELETE = (AppiumBy.ID, "android:id/button1")

    @staticmethod
    def language_by_name(name):
        return (
            AppiumBy.XPATH,
            f'//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/wiki_language_title" and @text="{name}"]'
        )

    @staticmethod
    def language_by_name_search(name):
        return (
            AppiumBy.XPATH,
            f'//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/localized_language_name" and @text="{name}"]'
        )

    def log(self, level, msg):
        if self.logger:
            getattr(self.logger, level)(msg)

    def choose_random_language(self, max_scrolls=20, click_fact=True):
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
            return language_name

        except Exception as e:
            self.log('error', f"❌ Ошибка при выборе языка: {str(e)}")
            return None

    def add_language_via_search(self, language_name):
        """Добавление языка через поле поиска"""
        try:
            self.log("debug", "Открытие поля поиска")
            if not self.clicks.safe_click(self.SEARCH_FIELD):
                self.log("warning", f"⚠️ Не удалось открыть поле поиска")
                return False

            self.log("debug", f"Ввод '{language_name}' в поле поиска")
            if not self.text.safe_input(self.INPUT_TEXT_FIELD, language_name):
                self.log("warning", f"⚠️ Не удалось ввести '{language_name}' в поле поиска")
                return False

            self.log("debug", f"Выбираем '{language_name}' в результатах поиска")
            result_locator = self.language_by_name_search(language_name)
            if not self.clicks.safe_click(result_locator):
                self.log("warning", f"⚠️ Язык '{language_name}' не найден в результатах поиска")
                return False

            return language_name

        except Exception as e:
            self.log("error", f"❌ Ошибка при добавлении языка: {str(e)}")
            return False

    def get_language_names(self):
        """
        Возвращает список языков, отображаемых на экране
        """
        self.clicks.wait_for_element(self.FIND_LANGUAGE_TITLE)
        elements = self.driver.find_elements(*self.FIND_LANGUAGE_TITLE)
        names = [el.text.strip() for el in elements if el.text.strip()]
        return names

    def wait_language(self, language_name):
        wait_lang = (
            AppiumBy.XPATH,
            f'//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/wiki_language_title" and @text="{language_name}"]'
        )
        self.clicks.wait_for_element(wait_lang)

    def move_language_to_bottom(self, language_name, new_language=None):
        """
        Перемещает язык с заданным названием в самый низ списка
        """
        try:
            self.log("debug", "Получаем текущий список языков")
            self.wait_language(language_name)
            if new_language:
                WebDriverWait(self.driver, 5).until(
                    lambda d: self.get_language_names()[-2] != 'English'
                    and self.get_language_names()[-2] != 'Русский'
                )
            languages = self.get_language_names()
            if not languages:
                self.log("warning", "⚠️ Список языков пуст или не получен")
                return False

            if language_name not in languages:
                self.log("warning", f"⚠️ Язык '{language_name}' не найден в списке")
                return False

            index_from = languages.index(language_name)
            index_to = len(languages) - 2  # Переместить в конец

            if index_from == index_to:
                self.log("info", f"✅ Язык '{language_name}' уже находится внизу списка")
                return True

            self.log("debug", "Получаем drag-элементы на экране")
            drag_elements = self.driver.find_elements(*self.DRAG_ICONS)

            if index_from >= len(drag_elements) or index_to >= len(drag_elements):
                self.log("error", "❌ Недостаточно drag-элементов для выполнения действия")
                return False

            source = drag_elements[index_from]
            target = drag_elements[index_to]

            self.log("debug", f"🔄 Перетаскиваем '{language_name}' с позиции {index_from} на {index_to}")
            self.driver.drag_and_drop(source, target)
            WebDriverWait(self.driver, 5).until(
                lambda d: self.get_language_names()[-2] == language_name
            )

            return True

        except Exception as e:
            self.log("error", f"❌ Ошибка при перемещении языка: {e}")
            return False

    def remove_random_language_by_long_press(self):
        try:
            self.log("debug", "Получаем текущий список языков")
            languages = self.get_language_names()
            if len(languages) <= 1:
                self.log("warning", "⚠️ Недостаточно языков для удаления")
                return False

            language_name = random.choice(languages[:-1])
            self.log("info", f"🎯 Выбран язык для удаления: '{language_name}'")

            self.wait_language(language_name)
            self.log("debug", "Ищем элемент выбранного языка")
            element = self.driver.find_element(*self.language_by_name(language_name))

            self.log("debug", f"Выполняем долгое нажатие на язык '{language_name}'")
            if not self.clicks.long_press(element):
                self.log("warning", "⚠️ Не удалось выполнить долгое нажатие")
                return False
            self.log("info", f"✅ Долгое нажатие выполнено для языка '{language_name}'")

            self.log("debug", "Подтверждаем удаление языка")
            if not self.clicks.safe_click(self.DELETE_BUTTOM):
                self.log("warning", "⚠️ Не удалось нажать кнопку удаления")
                return False
            if not self.clicks.safe_click(self.OK_DELETE):
                self.log("warning", "⚠️ Не удалось подтвердить удаление")
                return False

            self.log("info", f"🗑️ Язык '{language_name}' успешно удалён")

            return language_name

        except Exception as e:
            self.log("error", f"❌ Ошибка при удалении языка через long press: {e}")
            return False

    def remove_random_language_via_menu(self):
        try:
            self.log("debug", "Получаем текущий список языков")
            languages = self.get_language_names()
            if len(languages) <= 1:
                self.log("warning", "⚠️ Недостаточно языков для удаления")
                return False

            language_name = random.choice(languages[:-1])
            self.log("info", f"🎯 Выбран язык для удаления через меню: '{language_name}'")

            self.log("debug", "Открываем меню (три точки)")
            if not self.clicks.safe_click(self.MENU_BTN):
                self.log("warning", "⚠️ Не удалось открыть меню")
                return False

            self.log("debug", "Нажимаем 'Remove language'")
            if not self.clicks.safe_click(self.REMOVE_LANGUAGE_BTN):
                self.log("warning", "⚠️ Не удалось нажать 'Remove language'")
                return False

            self.log("debug", f"Выбираем язык '{language_name}' для удаления")
            checkbox_locator = self.language_by_name(language_name)
            if not self.clicks.safe_click(checkbox_locator):
                self.log("warning", f"⚠️ Не удалось выбрать язык '{language_name}'")
                return False

            self.log("debug", "Нажимаем на кнопку удаления")
            if not self.clicks.safe_click(self.DELETE_BUTTOM):
                self.log("warning", "⚠️ Не удалось нажать кнопку удаления")
                return False

            self.log("debug", "Подтверждаем удаление")
            if not self.clicks.safe_click(self.OK_DELETE):
                self.log("warning", "⚠️ Не удалось подтвердить удаление")
                return False

            self.log("info", f"🗑️ Язык '{language_name}' успешно удалён через меню")

            return language_name

        except Exception as e:
            self.log("error", f"❌ Ошибка при удалении языка через меню: {e}")
            return False