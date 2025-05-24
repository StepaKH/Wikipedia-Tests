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
    SCREEN_5 = {
        "locator": (AppiumBy.ID, 'org.wikipedia.alpha:id/wikipedia_languages_recycler')
    }
    SCREEN_6 = {
        "locator": (AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="org.wikipedia.alpha:id/languages_list_recycler"]/android.widget.LinearLayout[1]')
    }
    SCREEN_7 = {
        "locator": (AppiumBy.ID, 'org.wikipedia.alpha:id/scrollView')
    }

    def __init__(self, driver, logger=None):
        super().__init__(driver, logger=logger)
