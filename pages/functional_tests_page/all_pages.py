from pages.functional_tests_page.onboarding_pages.onboarding_page import OnboardingPage
from pages.functional_tests_page.saved_pages.saved_page import SavedPage
from pages.functional_tests_page.general_page.add_delete_language_page import LanguageActions
from pages.functional_tests_page.general_page.auth_reg_page import LoggingActions

class AllPages:
    def __init__(self, driver, logger=None):
        self.driver = driver
        self.onboarding = OnboardingPage(driver, logger=logger)
        self.saved = SavedPage(driver, logger=logger)
        self.language = LanguageActions(driver, logger=logger)
        self.logging = LoggingActions(driver, logger=logger)