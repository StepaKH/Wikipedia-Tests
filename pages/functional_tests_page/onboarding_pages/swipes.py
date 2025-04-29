from pages.functional_tests_page.base.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class OnboardingSwipes(BasePage):
    SCREEN_1 = {
        "locator": (
        AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/secondaryTextView"]'),
        "expected_text": "We’ve found the following on your device:"
    }
    SCREEN_2 = {
        "locator": (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/primaryTextView"]'),
        "expected_text": "New ways to explore"
    }
    SCREEN_3 = {
        "locator": (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/primaryTextView"]'),
        "expected_text": "Reading lists with sync"
    }
    SCREEN_4 = {
        "locator": (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/primaryTextView"]'),
        "expected_text": "Data & Privacy"
    }

    def __init__(self, driver):
        super().__init__(driver)