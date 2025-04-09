import pytest
from drivers.appium_driver import create_driver
from pages.functional_tests_page.onboarding_pages.onboarding_page import OnboardingPage

@pytest.fixture
def driver():
    d = create_driver()
    yield d
    d.quit()

@pytest.fixture
def onboarding(driver):
    return OnboardingPage(driver)