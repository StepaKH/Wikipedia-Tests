from pages.functional_tests_page.onboarding_pages.onboarding_page import OnboardingPage

class AllPages:
    def __init__(self, driver, logger=None):
        self.driver = driver
        self.onboarding = OnboardingPage(driver, logger=logger)