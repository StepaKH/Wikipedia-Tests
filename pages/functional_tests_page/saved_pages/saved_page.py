import random
import string
from appium.webdriver.common.appiumby import AppiumBy
from pages.functional_tests_page.base.base_page import BasePage

class SavedPage(BasePage):
    def __init__(self, driver, logger=None):
        super().__init__(driver, logger=logger)
        self.logger = logger

    # Protected Locators
    POSITIVE_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='org.wikipedia.alpha:id/positiveButton']")
    NEGATIVE_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='org.wikipedia.alpha:id/negativeButton']")
    EMPTY_TITLE_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/empty_title']")
    MESSAGE_TITLE_VIEW_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/messageTitleView']")
    CONTAINER_CLICK_AREA = (AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='org.wikipedia.alpha:id/containerClickArea']")
    FILTER_MY_LISTS_BTN = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Filter my lists']")
    MORE_OPTIONS_BTN = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='More options']")
    SORT_OPTIONS_LIST_RV = (AppiumBy.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id='org.wikipedia.alpha:id/sort_options_list']")
    CANCEL_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='android:id/button2']")
    BROWSE_FILES_IN_OTHER_APPS_TV = (AppiumBy.XPATH, "//android.widget.TextView[@text='BROWSE FILES IN OTHER APPS']")
    CREATE_AN_ACCOUNT_TV = (AppiumBy.XPATH, "//android.widget.TextView[@text='Create an account']")
    NAVIGATE_UP_BTN = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")
    SAVED_BTN = (AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Saved']")
    ACTION_MODE_BAR_VG = (AppiumBy.XPATH, "//android.view.ViewGroup[@resource-id='org.wikipedia.alpha:id/action_mode_bar']")

    #для залогиненого
    REFRESH_SYNC_TV = (AppiumBy.XPATH, "//android.widget.TextView[@text='Refresh sync']")
    NOTIFICATIONS_BTN = (AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Notifications']")
    ALL_NTF_BTN = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'All')]")
    MENTIONS_NTF_BTN = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Mentions')]")
    #NAVIGATE_UP_BTN = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")

    #for skip_onboarding
    CONTINUE_BTN = (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
    GET_STARTED_BTN = (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button")

    SEARCH_SRC_TEXT_ACTV = (AppiumBy.XPATH, "//android.widget.AutoCompleteTextView[@resource-id='org.wikipedia.alpha:id/search_src_text']")

    #for log_in
    CREATE_ACCOUNT_LOGIN_BUTTON_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='org.wikipedia.alpha:id/create_account_login_button']")
    LOGIN_BUTTON_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='org.wikipedia.alpha:id/login_button']")
    PERMISSION_DENY_BUTTON_BTN = (AppiumBy.XPATH,"//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_deny_button']")
    USERNAME_ET = (AppiumBy.XPATH, "//android.widget.EditText[@text='Username']")
    PASSWORD_ET = (AppiumBy.XPATH, "//android.widget.EditText[@text='Password']")

    #for log_out
    MORE_BTN = (AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='More']")
    SETTINGS_TV = (AppiumBy.XPATH, "//android.widget.TextView[@text='Settings']")
    LOGOUT_BUTTON_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='org.wikipedia.alpha:id/logoutButton']")
    BUTTON1_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='android:id/button1']")

    #for import_list
    IMPORT_LIST_TV = (AppiumBy.XPATH,"//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/reading_lists_overflow_import_list']")
    LARGE_FILES_BTN = (AppiumBy.XPATH, "//android.widget.Button[@text='Large files']")

    #for sort_by
    SORT_BY_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/reading_lists_overflow_sort_by']")
    SORT_BY_NAME_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/sort_type' and @text='Sort by name']")
    SORT_BY_NAME_REVERSE_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/sort_type' and @text='Sort by name (reverse)']")
    SORT_BY_DATE_CREATED_NEWEST_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/sort_type' and @text='Sort by date created (newest)']")
    SORT_BY_DATE_CREATED_OLDEST_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/sort_type' and @text='Sort by date created (oldest)']")
    SORT_BY_IV = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Sort by']")

    #for create new list
    CREATE_NEW_LIST_TV = (AppiumBy.XPATH,"//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/reading_lists_overflow_create_new_list']")
    TEXT_INPUT_ET = (AppiumBy.XPATH,"//android.widget.EditText[@resource-id='org.wikipedia.alpha:id/text_input']")
    SECONDARY_TEXT_INPUT_ET = (AppiumBy.XPATH,"//android.widget.EditText[@resource-id='org.wikipedia.alpha:id/secondary_text_input']")
    CANCEL_BUTTON2_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='android:id/button2']")
    OK_BUTTON1_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='android:id/button1']")

    #for long click on list
    EDIT_NAME_DESCRIPTION_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/title' and @text='Edit name/description']")
    SELECT_1_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/title' and @text='Select']")
    DELETE_LIST_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/title' and @text='Delete list']")
    SAFE_ALL_FOR_OFFLINE_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/title' and @text='Save all for offline']")
    REMOVE_ALL_FROM_OFFLINE = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/title' and @text='Remove all from offline']")
    EXPORT_LIST_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/title' and @text='Export list']")
    SHARE_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/title' and @text='Share…']")
    BLUETOOTH_TV = ( AppiumBy.XPATH, "//android.widget.TextView[@resource-id='android:id/text1' and @text='Bluetooth']")#swapdown

    #for delete list
    #OK_BUTTON1_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='android:id/button1']")
    #CANCEL_BUTTON2_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='android:id/button2']")
    SNACKBAR_TEXT_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/snackbar_text']")

    #for select
    SELECT_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/reading_lists_overflow_select']")
    UNCHECK_ALL_ITEMS_BTN = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Uncheck all items']")
    DELETE_SELECT_ITEMS_BTN = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Delete selected items']")
    MENU_EXPORT_SELECTED_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='org.wikipedia.alpha:id/menu_export_selected']")
    CHECK_ALL_ITEMS_BTN = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Check all items']")
    DONE_IV = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Done']")

    test_primary = {}
    test_secondary = {}
    i_primary = 1
    i_secondary = 1

    def log(self, level, msg):
                if self.logger:
                    getattr(self.logger, level)(msg)

    def test_text_input_works(self):
        test_text = self.test_primary[2]
        self.log("debug", f"=== Попытка ввода текста '{test_text}' ===")

        try:
            self.log("debug", f"Ввод '{test_text}' в поле фильтрации")
            if not self.text.safe_input(self.SEARCH_SRC_TEXT_ACTV, test_text):
                self.log("warning", f"⚠️ Не удалось ввести '{test_text}' в поле фильтрации")
                return False
            else: self.log("debug", f"Текст '{test_text}' введен успешно")

            return True


        except Exception as e:
            self.log("error", f"❌ Критическая ошибка при вводе текста: {str(e)}")
            return False

    def log_in_to_account(self):
        username = "leviofan2005"
        password = "08.06.05"

        try:
            self.log("debug", f"Ввод '{username}' в поле логина")
            if not self.text.safe_input(self.USERNAME_ET, username):
                self.log("warning", f"⚠️ Не удалось ввести '{username}' в поле логина")
                return False
            else: self.log("debug", f"Текст '{username}' введен успешно в поле логина")

            self.log("debug", f"Ввод '{password}' в поле пароля")
            if not self.text.safe_input(self.PASSWORD_ET, password):
                self.log("warning", f"⚠️ Не удалось ввести '{password}' в поле пароля")
                return False
            else:
                self.log("debug", f"Текст '{password}' введен успешно в поле пароля")

            return True

        except Exception as e:
            self.log("error", f"❌ Критическая ошибка при вводе текста: {str(e)}")
            return False

    def delete_array(self):
        self.test_primary.clear()
        self.test_secondary.clear()
        self.i_primary = 1
        self.i_secondary = 1

    def test_text_input_for_create_new_list(self):
        test_primary_text = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
        test_secondary_text = ''.join(random.choice(string.ascii_lowercase) for _ in range(20))
        self.test_primary[self.i_primary] = test_primary_text
        self.test_secondary[self.i_secondary] = test_secondary_text
        self.i_primary = self.i_primary + 1
        self.i_secondary = self.i_secondary + 1
        try:
            self.log("debug", f"=== Попытка ввода текста '{test_primary_text}' ===")

            self.log("debug", f"Ввод '{test_primary_text}' в поле фильтрации")
            if not self.text.safe_input(self.TEXT_INPUT_ET, test_primary_text):
                self.log("warning", f"⚠️ Не удалось ввести '{test_primary_text}' в поле фильтрации")
                return False
            else: self.log("debug", f"Текст '{test_primary_text}' введен успешно")

            self.log("debug", f"=== Попытка ввода текста '{test_secondary_text}' ===")

            self.log("debug", f"Ввод '{test_secondary_text}' в поле фильтрации")
            if not self.text.safe_input(self.SECONDARY_TEXT_INPUT_ET, test_secondary_text):
                self.log("warning", f"⚠️ Не удалось ввести '{test_secondary_text}' в поле фильтрации")
                return False
            else:
                self.log("debug", f"Текст '{test_secondary_text}' введен успешно")

            return True


        except Exception as e:
            self.log("error", f"❌ Критическая ошибка при вводе текста: {str(e)}")
            return False

    def check_add_list(self):

        try:
            self.log("debug", f"=== Попытка найти добавленный лист на экране 'saved' ===")
            if self.i_primary == 1:
               TITLE_ACTIVITI_VG = (AppiumBy.XPATH, "(//android.view.ViewGroup[@resource-id='org.wikipedia.alpha:id/item_title_container'])")
            else: TITLE_ACTIVITI_VG = (AppiumBy.XPATH, f"(//android.view.ViewGroup[@resource-id='org.wikipedia.alpha:id/item_title_container'])[{self.i_primary-1}]")

            if not self.clicks.is_visible(TITLE_ACTIVITI_VG):
                self.log("warning", f"⚠️ Не удалось найти лист '{self.test_primary[self.i_primary-1]}' на экране 'saved'")
                return False
            else: self.log("debug", f"Заголовок листа '{self.test_primary[self.i_primary-1]}' найден успешно")

            DESCRIPTION_ACTIVITI_TV = (AppiumBy.XPATH, f"//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/item_description' and @text='{self.test_secondary[self.i_secondary-1]}']")

            if not self.clicks.is_visible(DESCRIPTION_ACTIVITI_TV):
                self.log("warning", f"⚠️ Не удалось найти лист '{self.test_secondary[self.i_secondary-1]}' на экране 'saved'")
                return False
            else:
                self.log("debug", f"Лист '{self.test_secondary[self.i_secondary-1]}' найден успешно")

            return True


        except Exception as e:
            self.log("error", f"❌ Критическая ошибка при проврке текста: {str(e)}")
            return False

    def create_list(self):

        try:
            self.log( "info", "Нажатие кнопки 'more'")
            assert self.clicks.safe_click(self.MORE_OPTIONS_BTN), "Кнопка 'more' не найдена"
            self.log("info","Кнопка 'more' найдена и нажата")
            self.log("info", "Нажатие кнопки 'create_new_list'")
            self.log("info", "Ищем кнопку 'create_new_list'")
            assert self.clicks.safe_click(self.CREATE_NEW_LIST_TV), "Кнопка 'create_new_list' не найдена"
            self.log("info", "Кнопка 'create_new_list' найдена и нажата")
            self.log("debug", "Проверяем, что экран кнопки 'create_new_list' отобразился на экране")
            assert self.clicks.is_visible(self.TEXT_INPUT_ET), "Экран кнопки 'create_new_list' не отобразился на экране"
            self.log("info", "Экран кнопки 'create_new_list' отобразился на экране")
            self.log("info", "Ввод данных названий в лист (основное и description)")
            assert self.test_text_input_for_create_new_list(), "Не удалось ввести данные"
            self.log("info", "Данные введены успешно")
            self.log("info", "Нажатие кнопки 'ok'")
            assert self.clicks.safe_click(self.OK_BUTTON1_BTN), "Кнопка 'ok' не найдена"
            self.log("info", "Кнопка 'ok' нажата")
            self.log("debug", "Проверяем, что лист с введенными названиями добавился")
            assert self.check_add_list(), "Лист с введенными названиями не добавился"
            self.log("info", "Лист с введенными названиями добавился")

            return  True

        except Exception as e:
            self.log("error", f"❌ Критическая ошибка при проврке текста: {str(e)}")
            return False

    def press_to_title_activity(self):
        try:
            print(self.i_primary)
            if self.i_primary == 1:
               TITLE_ACTIVITI_VG = (AppiumBy.XPATH, "(//android.view.ViewGroup[@resource-id='org.wikipedia.alpha:id/item_title_container'])")
            else: TITLE_ACTIVITI_VG = (AppiumBy.XPATH, f"(//android.view.ViewGroup[@resource-id='org.wikipedia.alpha:id/item_title_container'])[{self.i_primary-1}]")
            element = self.driver.find_element(*TITLE_ACTIVITI_VG)
            self.clicks.long_press(element)
            return  True

        except Exception as e:
            self.log("error", f"❌ Критическая ошибка при нажатии на лист: {str(e)}")
            return False

    def title_actv_is_visible(self):
        if self.i_primary == 1:
            TITLE_ACTIVITI_VG = (AppiumBy.XPATH, "(//android.view.ViewGroup[@resource-id='org.wikipedia.alpha:id/item_title_container'])")
        else: TITLE_ACTIVITI_VG = (AppiumBy.XPATH, f"(//android.view.ViewGroup[@resource-id='org.wikipedia.alpha:id/item_title_container'])[{self.i_primary - 1}]")
        assert self.clicks.is_visible(TITLE_ACTIVITI_VG)
        return True

    def sort_array_by_name(self):
        names = list(self.test_primary.values())  # получаем все названия листов
        return sorted(names)

    def reverse_sort_array_by_name(self):
        names = list(self.test_primary.values())  # получаем все названия листов
        return sorted(names, reverse=True)

    def sort_array_by_data(self):
        return list(self.test_primary.values())

    def reverse_sort_array_by_data(self):
        return list(self.test_primary.values())[::-1]

    def get_list_names(self):
        """Возвращает названия всех листов в виде списка."""
        LIST_ITEMS_XPATH = "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/item_title']"
        self.clicks.wait_for_element((AppiumBy.XPATH, LIST_ITEMS_XPATH))
        elements = self.driver.find_elements(AppiumBy.XPATH, LIST_ITEMS_XPATH)
        return [el.text.strip() for el in elements if el.text.strip()]