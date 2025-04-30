from pages.functional_tests_page.onboarding_pages.onboarding_page import OnboardingPage
from pages.functional_tests_page.saved_pages.saved_page import SavedPage

class AllPages:
    def __init__(self, driver, logger=None):
        self.driver = driver
        self.onboarding = OnboardingPage(driver, logger=logger)
        self.saved = SavedPage(driver)
