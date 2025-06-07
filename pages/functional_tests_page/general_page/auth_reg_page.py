from appium.webdriver.common.appiumby import AppiumBy
from pages.functional_tests_page.base.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait

class LoggingActions(BasePage):
    def __init__(self, driver, logger=None):
        super().__init__(driver, logger=logger)
        self.logger = logger

    MENU_BUTTOM = (AppiumBy.ACCESSIBILITY_ID, "More")
    MAIN_LOGIN_BUTTOM = (AppiumBy.ID, "org.wikipedia.alpha:id/main_drawer_login_button")
    LOG_IN_BUTTOM = (AppiumBy.ID, "org.wikipedia.alpha:id/create_account_login_button")
    JOIN_WIKIPEDIA_BUTTOM = (AppiumBy.ID, "org.wikipedia.alpha:id/login_create_account_button")
    LOGIN_SCREEN = (AppiumBy.XPATH, '//android.widget.TextView[@text="Log in"]')
    JOIN_WIKIPEDIA_SCREEN = (AppiumBy.XPATH, '//android.widget.TextView[@text="Create an account"]')
    BACK_BTN = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")
    MAIN_SCREEN = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.LinearLayout')

    USERNAME_INPUT = (AppiumBy.XPATH, '//android.widget.EditText[@text="Username"]')
    PASSWORD_INPUT = (AppiumBy.XPATH, '//android.widget.EditText[@text="Password"]')
    REPEAT_PASSWORD_INPUT = (AppiumBy.XPATH, '//android.widget.EditText[@text="Repeat password"]')
    EMAIL_INPUT = (AppiumBy.XPATH, '//android.widget.EditText[@text="Email (Optional)"]')

    ERROR_CODE = (AppiumBy.ACCESSIBILITY_ID, "Error")
    CONTINUE_BUTTOM = (AppiumBy.ID, "org.wikipedia.alpha:id/create_account_submit_button")

    CONTINUE_WITHOUT_EMAIL_BTN = (AppiumBy.ID, "android:id/button1")
    ENTER_EMAIL_BTN = (AppiumBy.ID, "android:id/button2")
    CAPTCHA_SUBMIT_BTN = (AppiumBy.ID, "org.wikipedia.alpha:id/captcha_submit_button")
    EMAIL_WARNING_DIALOG = (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout')

    LOGIN_FIELD = (AppiumBy.XPATH, '//android.widget.EditText[@text="Username"]')
    PASSWORD_FIELD = (AppiumBy.XPATH, '//android.widget.EditText[@text="Password"]')
    LOGIN_BUTTON = (AppiumBy.ID, "org.wikipedia.alpha:id/login_button")
    ERROR_MESSAGE = (AppiumBy.ID, "org.wikipedia.alpha:id/snackbar_text")
    SUCCESS_LOGIN_INDICATOR = (AppiumBy.ID, "com.android.permissioncontroller:id/grant_dialog")
    PERMISSION_DENY_BUTTON_BTN = (AppiumBy.XPATH,"//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_deny_button']")

    def go_to_login_screen(self):
        self.logger.debug("Переход в экран Log in")
        assert self.clicks.safe_click(self.LOG_IN_BUTTOM), "❌ Кнопка 'Log in' не найдена"
        assert self.clicks.is_visible(self.LOGIN_SCREEN), "❌ Не перешли на экран 'Log in'"
        self.logger.info("Нажали на кнопку 'Log in' и перешли на нужный экран")

    def go_to_main_screen(self, direction: str, from_screen):
        swipe = self.swipes.swipe_left if direction == "left" else self.swipes.swipe_right
        self.logger.debug(f"Свайп {direction} на главный экран")
        assert swipe(
            wait_locator=self.MAIN_SCREEN,
            first_screen=from_screen,
            speed='fast'
        ), f"Не удалось перейти на главный экран свайпом {direction}"
        self.logger.info("✅ Успешно перешли на главный экран")

    def fill_registration_form(self, username, password=None, repeat_password=None, email=None):
        self.logger.debug("Заполняем форму регистрации")
        assert self.text.safe_input(self.USERNAME_INPUT, username), "❌ Не удалось ввести имя пользователя"
        if password:
            assert self.text.safe_input(self.PASSWORD_INPUT, password), "❌ Не удалось ввести пароль"
        if repeat_password:
            assert self.text.safe_input(self.REPEAT_PASSWORD_INPUT, repeat_password), "❌ Не удалось повторить пароль"
        if email is not None:
            assert self.text.safe_input(self.EMAIL_INPUT, email), "❌ Не удалось ввести email"
        self.logger.info("Заполнили форму регистрации")

    def fill_auth_form(self, login, password):
        self.logger.debug("Заполняем форму авторизации")
        assert self.text.safe_input(self.USERNAME_INPUT, login), "❌ Не удалось ввести имя пользователя"
        assert self.text.safe_input(self.PASSWORD_INPUT, password), "❌ Не удалось ввести пароль"
        self.logger.info("Заполнили форму авторизации")