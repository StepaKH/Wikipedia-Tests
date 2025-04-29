from appium.webdriver.common.appiumby import AppiumBy
from pages.functional_tests_page.base.base_page import BasePage

class OnboardingButtons(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Protected Locators
    CONTINUE_BTN = (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
    GET_STARTED_BTN = (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button")
    SKIP_BTN = (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")
    ADD_LANGUAGE_BTN = (AppiumBy.ID, "org.wikipedia.alpha:id/addLanguageButton")
    MAIN_SCREEN = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.LinearLayout")
    ADD_LANGUAGE_ITEM = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/wiki_language_title' and @text='Add language']")
    NAVIGATE_UP_BTN = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")