import pytest
import allure

@pytest.mark.onboarding
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