from selenium.common.exceptions import TimeoutException
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
        try:
            return self.wait_for_element(by_locator).is_displayed()
        except TimeoutException:
            return False

    def safe_click(self, by_locator):
        """Ожидание видимости элемента и клик по нему"""
        element = self.is_visible(by_locator)
        if element:
            self.click(by_locator)
        return element

    def long_press(self, by_locator, duration=2000):
        """Долгое нажатие на элемент (по умолчанию 2 секунды)"""
        try:
            self.driver.execute_script('mobile: longClickGesture', {
                'elementId': by_locator.id,
                'duration': duration
            })
            return True
        except Exception as e:
            return False

    def drag_and_drop_elm(self, source_locator, target_locator):
        """Перетаскивание одного элемента на другой"""
        source = self.wait_for_element(source_locator)
        target = self.wait_for_element(target_locator)

        self.driver.drag_and_drop(source, target)

        self.wait_for_element(source_locator)
        self.wait_for_element(target_locator)