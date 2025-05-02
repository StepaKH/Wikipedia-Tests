from pages.functional_tests_page.base.actions.click_actions import ClickActions
from pages.functional_tests_page.base.actions.swipe_actions import SwipeActions
from pages.functional_tests_page.base.actions.text_actions import TextActions

class BasePage:
    def __init__(self, driver, timeout=10, logger=None):
        self.driver = driver
        self.clicks = ClickActions(driver, timeout)
        self.swipes = SwipeActions(driver, timeout, logger)
        self.text = TextActions(driver, timeout)