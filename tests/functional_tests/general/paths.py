import pytest
import allure

@pytest.fixture(scope="function")
def open_language_edit_screen(pages, logger):
    """Фикстура для перехода на экран редактирования языков"""
    onboarding = pages.onboarding.buttons
    lang_page = pages.language

    with allure.step("🛠 Setup: Переход на экран изменения языков"):
        logger.debug("Переход на экран редактирования языков ('Add or edit languages')")
        assert onboarding.clicks.safe_click(onboarding.ADD_LANGUAGE_BTN), \
            "❌ Кнопка 'Add or edit languages' не найдена"
        logger.info("✅ Экран редактирования языков успешно открыт")

    return lang_page
