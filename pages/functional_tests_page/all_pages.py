from pages.functional_tests_page.onboarding_pages.onboarding_page import OnboardingPage
from pages.functional_tests_page.saved_pages.saved_page import SavedPage

class AllPages:
    def __init__(self, driver):
        self.driver = driver
        self.onboarding = OnboardingPage(driver)
        self.saved = SavedPage(driver)