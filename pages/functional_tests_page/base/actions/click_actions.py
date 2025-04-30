from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ClickActions:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def click(self, by_locator):
        self.wait_for_element(by_locator).click()

    def is_visible(self, by_locator):
        return self.wait_for_element(by_locator).is_displayed()

    def safe_click(self, by_locator):
        """Ожидание видимости элемента и клик по нему"""
        element = self.is_visible(by_locator)
        if element:
            self.click(by_locator)
        return element