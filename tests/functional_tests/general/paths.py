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

@pytest.fixture(scope="function")
def open_log_in_screen(pages, logger):
    with allure.step("⏭️ Пропуск онбординга"):
        try:
            onboarding = pages.onboarding.buttons
            for i in range(3):
                if onboarding.clicks.safe_click(onboarding.CONTINUE_BTN):
                    logger.debug(f"Пропускаем экран {i + 1}")

            if onboarding.clicks.safe_click(onboarding.GET_STARTED_BTN):
                logger.debug("Нажата кнопка 'Get Started'")

        except Exception as e:
            logger.warning(f"Онбординг не был полностью показан или уже пропущен: {str(e)}")

    with allure.step('Переход во вкладку "Log in / join Wikipedia"'):
        try:
            logging = pages.logging

            logger.debug('Переход во ввкладку "Меню"')
            assert logging.clicks.safe_click(logging.MENU_BUTTOM), "❌ Кнопка 'Меню' не найдена"

            logger.debug('Переход во вкладку "Log in / join Wikipedia"')
            assert logging.clicks.safe_click(logging.MAIN_LOGIN_BUTTOM)
            logger.info('✅ Экран успешно открыт')

        except Exception as e:
            logger.warning(f"Переход во вкладку не был реализован: {str(e)}")

    return pages.logging