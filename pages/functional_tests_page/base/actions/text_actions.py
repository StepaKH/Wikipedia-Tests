from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TextActions:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element(self, by_locator):
        """Ожидание появления элемента (input-поля)"""
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def clear_text(self, by_locator):
        """Очистка поля ввода"""
        element = self.wait_for_element(by_locator)
        element.clear()
        return element

    def get_text(self, by_locator):
        """Получить текст из поля или элемента"""
        return self.wait_for_element(by_locator).text

    def is_text_equal(self, by_locator, expected_text):
        """Проверка: текст в поле соответствует ожидаемому"""
        actual_text = self.get_text(by_locator)
        return actual_text == expected_text

    def safe_input(self, by_locator, text):
        """Безопасный ввод текста (если поле найдено)"""
        try:
            element = self.clear_text(by_locator)
            element.send_keys(text)
            return True
        except Exception as e:
            return False