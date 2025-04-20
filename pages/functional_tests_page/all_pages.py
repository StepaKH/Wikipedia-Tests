from pages.functional_tests_page.onboarding_pages.onboarding_page import OnboardingPage

class AllPages:
    def __init__(self, driver):
        self.driver = driver
        self.onboarding = OnboardingPage(driver)