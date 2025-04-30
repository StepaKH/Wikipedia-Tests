from pages.functional_tests_page.saved_pages.saved_buttons import SavedButtons

class SavedPage:
    def __init__(self, driver):
        self.driver = driver
        self.buttons = SavedButtons(driver)