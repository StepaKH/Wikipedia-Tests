from pages.functional_tests_page.base.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class OnboardingSwipes(BasePage):
    _SCREENS = [
        {   # Экран 1 (начальный)
            "locator": (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/secondaryTextView"]'),
            "expected_text": "We’ve found the following on your device:"
        },
        {   # Экран 2
            "locator": (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/primaryTextView"]'),
            "expected_text": "New ways to explore"
        },
        {   # Экран 3
            "locator": (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/primaryTextView"]'),
            "expected_text": "Reading lists with sync"
        },
        {   # Экран 4
            "locator": (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/primaryTextView"]'),
            "expected_text": "Data & Privacy"
        }
    ]

    def __init__(self, driver):
        super().__init__(driver)
        self.screens = self._SCREENS

    def swipe_forward_to_screen(self, target_screen: int):
        """Один свайп влево с проверкой целевого экрана"""
        if not 2 <= target_screen <= 4:
            raise ValueError("Target screen must be between 2 and 4 for forward swipe")

        print(self.screens[target_screen - 1]["expected_text"])

        return self.swipes.swipe_left(self.screens[target_screen - 1]["locator"],
                                        self.screens[target_screen - 1]["expected_text"])

    def swipe_backward_to_screen(self, target_screen: int):
        """Один свайп вправо с проверкой целевого экрана"""
        if not 1 <= target_screen <= 3:
            raise ValueError("Target screen must be between 1 and 3 for backward swipe")

        return self.swipes.swipe_right(self.screens[target_screen - 1]["locator"],
                                self.screens[target_screen - 1]["expected_text"])