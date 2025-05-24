from pages.functional_tests_page.onboarding_pages.onboarding_page import OnboardingPage
from pages.functional_tests_page.saved_pages.saved_page import SavedPage
from pages.functional_tests_page.explore_pages.explore_page import ExplorePage

class AllPages:
    def __init__(self, driver, logger=None):
        self.driver = driver
        self.onboarding = OnboardingPage(driver, logger=logger)
        self.saved = SavedPage(driver, logger=logger)
        self.explore = ExplorePage(driver, logger=logger)