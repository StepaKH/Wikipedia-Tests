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
    SELECT_TV = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/reading_lists_overflow_select']")
    SORT_BY_TV = (AppiumBy.XPATH,"//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/reading_lists_overflow_sort_by']")
    CREATE_NEW_LIST_TV = (AppiumBy.XPATH,"//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/reading_lists_overflow_create_new_list']")
    IMPORT_LIST_TV = (AppiumBy.XPATH,"//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/reading_lists_overflow_import_list']")
    REFRESH_SYNC_TV = (AppiumBy.XPATH, "//android.widget.TextView[@text='Refresh sync']")
    CHECK_ALL_ITEMS_BTN = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Check all items']")
    DONE_IV = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Done']")
    SORT_OPTIONS_LIST_RV = (AppiumBy.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id='org.wikipedia.alpha:id/sort_options_list']")
    CANCEL_BTN = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='android:id/button2']")
    BROWSE_FILES_IN_OTHER_APPS_TV = (AppiumBy.XPATH, "//android.widget.TextView[@text='BROWSE FILES IN OTHER APPS']")
    CREATE_AN_ACCOUNT_TV = (AppiumBy.XPATH, "//android.widget.TextView[@text='Create an account']")
    NAVIGATE_UP_BTN = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")
    SAVED_BTN = (AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Saved']")
    ACTION_MODE_BAR_VG = (AppiumBy.XPATH, "//android.view.ViewGroup[@resource-id='org.wikipedia.alpha:id/action_mode_bar']")

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


    def log(self, level, msg):
                if self.logger:
                    getattr(self.logger, level)(msg)

    def test_text_input_works(self):
        test_text = "Test input"
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
        username = "Artv1dal"
        password = "08.06.2005"

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
