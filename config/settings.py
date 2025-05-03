import os

class Config:
    """Конфигурация проекта"""

    # Адрес Appium-сервера
    APPIUM_SERVER_URL = "http://localhost:4723"

    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    APP_PATH = os.path.join(PROJECT_ROOT, "apk", "app-alpha-debug.apk")

    # Настройки Appium
    PLATFORM_NAME = "Android"
    AUTOMATION_NAME = "uiautomator2"
    DEVICE_NAME = "emulator-5554"
    LANGUAGE = "en"
    LOCALE = "US"

    # Пакет и активности
    APP_PACKAGE = "org.wikipedia.alpha"
    APP_ACTIVITY = "org.wikipedia.main.MainActivity"

    # Другие активности
    ACTIVITIES = {
        "main": "org.wikipedia.main.MainActivity",
        "search": "org.wikipedia.search.SearchActivity",
        "page": "org.wikipedia.page.PageActivity",
    }