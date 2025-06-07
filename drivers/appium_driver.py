from appium import webdriver
from appium.options.android import UiAutomator2Options

from config.settings import Config


def create_driver(worker_id: str = "master"):
    device_config = Config.get_device_config(worker_id)

    # Формируем URL для Appium с учетом порта устройства
    appium_url = f"http://localhost:{device_config['appiumPort']}"

    options = UiAutomator2Options().load_capabilities({
        **device_config,
        "app": Config.APP_PATH,
        "appPackage": Config.APP_PACKAGE,
        "appActivity": Config.APP_ACTIVITY,
        "newCommandTimeout": 300,
        "uiautomator2ServerInstallTimeout": 60000,
        "adbExecTimeout": 60000,
        "autoGrantPermissions": True
    })

    return webdriver.Remote(appium_url, options=options)