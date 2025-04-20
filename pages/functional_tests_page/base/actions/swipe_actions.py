from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SwipeActions:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def swipe(self, direction: str, wait_locator=None, expected_text=None):
        # Приводим направление к нижнему регистру для унификации
        direction = direction.lower()

        # Получаем размеры экрана
        window_size = self.driver.get_window_size()
        width = window_size['width']
        height = window_size['height']

        # Определяем параметры свайпа в зависимости от направления
        if direction == 'left':
            start_x = width * 0.9
            end_x = width * 0.1
            start_y = height * 0.5
            end_y = height * 0.5
        elif direction == 'right':
            start_x = width * 0.1
            end_x = width * 0.9
            start_y = height * 0.5
            end_y = height * 0.5
        elif direction == 'up':
            start_x = width * 0.5
            end_x = width * 0.5
            start_y = height * 0.9
            end_y = height * 0.1
        elif direction == 'down':
            start_x = width * 0.5
            end_x = width * 0.5
            start_y = height * 0.1
            end_y = height * 0.9
        else:
            raise ValueError(f"Unsupported swipe direction: {direction}")

        self.driver.swipe(start_x, start_y, end_x, end_y, 500)

        if wait_locator:
            element = self.wait_for_element(wait_locator)
            if expected_text:
                actual = element.text.strip()
                return actual == expected_text
            return element.is_displayed()

        return True

    def swipe_left(self, wait_locator=None, expected_text=None):
        return self.swipe("left", wait_locator, expected_text)

    def swipe_right(self, wait_locator=None, expected_text=None):
        return self.swipe("right", wait_locator, expected_text)

    def swipe_up(self, wait_locator=None, expected_text=None):
        return self.swipe("up", wait_locator, expected_text)

    def swipe_down(self, wait_locator=None, expected_text=None):
        return self.swipe("down", wait_locator, expected_text)