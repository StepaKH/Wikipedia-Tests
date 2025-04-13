from appium.webdriver.common.appiumby import AppiumBy
from pages.functional_tests_page.base_page import BasePage

class OnboardingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Protected Locators
    _CONTINUE_BTN = (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
    _GET_STARTED_BTN = (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button")
    _SKIP_BTN = (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")
    _ADD_LANGUAGE_BTN = (AppiumBy.ID, "org.wikipedia.alpha:id/addLanguageButton")
    _MAIN_SCREEN = (
    AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.LinearLayout")
    _ADD_LANGUAGE_ITEM = (AppiumBy.XPATH,
                          "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/wiki_language_title' and @text='Add language']")
    _NAVIGATE_UP_BTN = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")

    # Tap methods
    def tap_continue(self):
        self.click(self._CONTINUE_BTN)

    def tap_skip(self):
        self.click(self._SKIP_BTN)

    def tap_get_started(self):
        self.click(self._GET_STARTED_BTN)

    def tap_add_language_button(self):
        self.click(self._ADD_LANGUAGE_BTN)

    def tap_add_language_in_list(self):
        self.click(self._ADD_LANGUAGE_ITEM)

    def tap_navigate_up(self):
        self.click(self._NAVIGATE_UP_BTN)

    # Visibility checkers
    def is_main_screen_visible(self):
        return self.is_visible(self._MAIN_SCREEN)

    def is_skip_button_visible(self):
        return self.is_visible(self._SKIP_BTN)

    def is_get_started_visible(self):
        return self.is_visible(self._GET_STARTED_BTN)

    def is_continue_button_visible(self):
        return self.is_visible(self._CONTINUE_BTN)

    def is_add_language_button_visible(self):
        return self.is_visible(self._ADD_LANGUAGE_BTN)

    def is_add_language_in_list_visible(self):
        return self.is_visible(self._ADD_LANGUAGE_ITEM)

    def is_navigate_up_visible(self):
        return self.is_visible(self._NAVIGATE_UP_BTN)