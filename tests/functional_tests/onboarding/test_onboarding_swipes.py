import pytest
import allure

@pytest.mark.onboarding
@pytest.mark.smoke
@allure.description("""
**Полный тест свайпов онбординга:**
""")
def test_full_onboarding_swipe_navigation(pages, logger):
    """Полная проверка навигации по онбордингу свайпами"""
    try:
        onboarding = pages.onboarding.swipes
        total_screens = 4  # Общее количество экранов онбординга
        logger.info("=== Начало теста: полная проверка свайпов онбординга ===")

        screens = [
            onboarding.SCREEN_1,
            onboarding.SCREEN_2,
            onboarding.SCREEN_3,
            onboarding.SCREEN_4
        ]

        # Проход вперед через все экраны
        with allure.step("1. Проход вперед через все экраны (1 → 4)"):
            for i in range(1, total_screens):
                with allure.step(f"1.{i}. Переход на экран {i + 1}"):
                    logger.debug(f"Свайп вперед на экран {i + 1}")
                    assert onboarding.swipes.swipe_left(
                        screens[i]["locator"],
                        screens[i]["expected_text"]
                    ), f"Не удалось перейти на экран {i + 1}"
                    logger.info(f"Успешно перешли на экран {i + 1}")

        # Проход назад через все экраны
        with allure.step("2. Проход назад через все экраны (4 → 1)"):
            for i in range(total_screens - 1, 0, -1):
                with allure.step(f"2.{total_screens - i}. Возврат на экран {i}"):
                    logger.debug(f"Свайп назад на экран {i}")
                    assert onboarding.swipes.swipe_right(
                        screens[i - 1]["locator"],
                        screens[i - 1]["expected_text"]
                    ), f"Не удалось вернуться на экран {i}"
                    logger.info(f"Успешно вернулись на экран {i}")

        logger.info("=== Тест успешно завершен: все свайпы работают корректно ===")

    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        allure.attach(
            name="Ошибка при выполнении теста",
            body=str(e),
            attachment_type=allure.attachment_type.TEXT
        )
        raise

@pytest.mark.onboarding
@pytest.mark.smoke
@allure.description("""
**Тест для проверки навигации по вкладке "Add or edit language":**
""")
def test_add_language_swipe_navigation(pages, logger):
    """Проверка свайпов на экранах добавления и редактирования языка"""
    try:
        onboarding = pages.onboarding
        logger.info("=== Начало теста: проверка свайпов во вкладке 'Add or edit language' ===")

        with allure.step("1. Переход в вкладку 'Add Language'"):
            logger.debug("Кликаем на кнопку 'Add or edit language' для перехода на экран добавления языка")
            onboarding.buttons.clicks.click(onboarding.buttons.ADD_LANGUAGE_BTN)
            logger.info("Успешно перешли в вкладку 'Add or edit language'")

            logger.debug("Кликаем на 'Add Language' для перехода на экран добавления языка")
            onboarding.buttons.clicks.click(onboarding.buttons.ADD_LANGUAGE_ITEM)
            logger.info("Успешно перешли в вкладку 'Add language'")

        with allure.step("2. Проверка возврата на экран с помощью свайпов"):
            # Левый свайп
            logger.debug("Проверка возврата на предыдущий экран с помощью свайпа влево")
            assert onboarding.swipes.swipes.swipe_left(
                wait_locator=onboarding.swipes.SCREEN_5["locator"],
                first_screen=onboarding.swipes.SCREEN_6["locator"],
                speed="fast"
            ), "Не удалось вернуться на экран"
            logger.info("Успешно вернулись на экран с помощью свайпа влево")

            logger.debug("Кликаем на 'Add Language' для обратного перехода на экран добавления языка")
            onboarding.buttons.clicks.click(onboarding.buttons.ADD_LANGUAGE_ITEM)
            logger.info("Успешно перешли в вкладку 'Add language'")

            # Правый свайп
            logger.debug("Проверка возврата на экран с помощью свайпа вправо")
            assert onboarding.swipes.swipes.swipe_right(
                wait_locator=onboarding.swipes.SCREEN_5["locator"],
                first_screen=onboarding.swipes.SCREEN_6["locator"],
                speed="fast"
            ), "Не удалось вернуться на экран с помощью свайпа вправо"
            logger.info("Успешно вернулись на экран с помощью свайпа вправо")

        with allure.step("3. Проверка возврата на экран с помощью свайпов в разделе 'Add or edit language'"):
            logger.debug("Проверка возврата с помощью свайпа вправо в 'Add or edit language'")
            assert onboarding.swipes.swipes.swipe_right(
                wait_locator=onboarding.swipes.SCREEN_7["locator"],
                first_screen=onboarding.swipes.SCREEN_5["locator"],
                speed="fast"
            ), "Не удалось вернуться на экран с помощью свайпа вправо"
            logger.info("Успешно вернулись на экран с помощью свайпа вправо")

            logger.debug("Кликаем на кнопку 'Add or edit language' для обратного перехода на экран добавления языка")
            onboarding.buttons.clicks.click(onboarding.buttons.ADD_LANGUAGE_BTN)
            logger.info("Успешно перешли в вкладку 'Add or edit language'")

            logger.debug("Проверка возврата на экран с помощью свайпа влево в 'Add or edit language'")
            assert onboarding.swipes.swipes.swipe_left(
                wait_locator=onboarding.swipes.SCREEN_7["locator"],
                first_screen=onboarding.swipes.SCREEN_5["locator"],
                speed="fast"
            ), "Не удалось вернуться на экран с помощью свайпа влево"
            logger.info("Успешно вернулись на экран с помощью свайпа влево")

        logger.info("=== Тест успешно завершен: все свайпы работают корректно ===")

    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        allure.attach(
            name="Ошибка при выполнении теста",
            body=str(e),
            attachment_type=allure.attachment_type.TEXT
        )
        raise
