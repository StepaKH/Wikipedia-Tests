from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SwipeActions:
    def __init__(self, driver, timeout=10, logger=None):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logger = logger

    def wait_for_element(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def swipe(self, direction: str, speed="normal", wait_locator=None, expected_text=None, first_screen=None):
        # Приводим направление к нижнему регистру для унификации
        direction = direction.lower()

        if self.logger:
            self.logger.debug(f"📲 Начинаем свайп: направление = {direction.upper()}")

        if first_screen:
            if self.logger:
                self.logger.info("⏳ Ожидание экрана перед свайпом")
            try:
                self.wait_for_element(first_screen)
            except Exception as e:
                if self.logger:
                    self.logger.warning("⚠️ Не удалось дождаться первого экрана")
                return False

        # Получаем размеры экрана
        window_size = self.driver.get_window_size()
        width = window_size['width']
        height = window_size['height']

        # Определяем параметры свайпа в зависимости от направления
        if direction == 'left':
            start_x = width * 0.9 if speed == "normal" else width
            end_x = width * 0.1
            start_y = height * 0.5
            end_y = height * 0.5
        elif direction == 'right':
            start_x = width * 0.1 if speed == "normal" else 0
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

        swipe_speed = 500 if speed == "normal" else 300  # 300 для быстрого свайпа

        # Выполнение свайпа
        self.driver.swipe(start_x, start_y, end_x, end_y, swipe_speed)

        if wait_locator:
            if self.logger:
                self.logger.info("🔍 Ожидание элемента после свайпа")
            try:
                element = self.wait_for_element(wait_locator)
                if expected_text:
                    actual = element.text.strip()
                    result = actual == expected_text
                    if self.logger:
                        if result:
                            self.logger.info(f"✅ Найден текст: '{actual}' соответствует ожидаемому.")
                        else:
                            self.logger.warning(f"⚠️ Текст не совпадает: '{actual}' ≠ '{expected_text}'")
                    return result
                return element.is_displayed()
            except Exception as e:
                if self.logger:
                    self.logger.warning(f"⚠️ Элемент не найден после свайпа: {str(e)}")
                return False

        return True

    def swipe_left(self, wait_locator=None, expected_text=None, first_screen=None, speed="normal"):
        return self.swipe("left", speed, wait_locator, expected_text, first_screen)

    def swipe_right(self, wait_locator=None, expected_text=None, first_screen=None, speed="normal"):
        return self.swipe("right", speed, wait_locator, expected_text, first_screen)

    def swipe_up(self, wait_locator=None, expected_text=None, first_screen=None, speed="normal"):
        return self.swipe("up", speed, wait_locator, expected_text, first_screen)

    def swipe_down(self, wait_locator=None, expected_text=None, first_screen=None, speed="normal"):
        return self.swipe("down", speed, wait_locator, expected_text, first_screen)

    def swipe_up_for_customize(self, wait_locator=None, expected_text=None, first_screen=None, speed="slow"):
        """
        Улучшенный свайп вверх с возможностью медленного скролла
        """
        window_size = self.driver.get_window_size()
        width = window_size['width']
        height = window_size['height']

        # Параметры для медленного свайпа
        if speed == "slow":
            start_y = height * 0.8  # Начинаем ниже
            end_y = height * 0.2  # Заканчиваем выше
            duration = 1000  # Более медленный свайп
        else:
            start_y = height * 0.7
            end_y = height * 0.3
            duration = 500

        self.driver.swipe(width * 0.5, start_y, width * 0.5, end_y, duration)

        if wait_locator:
            return self._check_swipe_result(wait_locator, expected_text)
        return True