from pages.functional_tests_page.onboarding_pages.buttons import OnboardingButtons
from pages.functional_tests_page.onboarding_pages.swipes import OnboardingSwipes

class OnboardingPage:
    def __init__(self, driver):
        self.driver = driver
        self.buttons = OnboardingButtons(driver)
        self.swipes = OnboardingSwipes(driver)