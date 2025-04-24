import pytest
import allure

@pytest.mark.onboarding
@allure.description("""
**Полный тест свайпов онбординга:**
1. Последовательно свайпаем вперед через все экраны (1 → 4)
2. Последовательно свайпаем назад через все экраны (4 → 1)
Для каждого перехода проверяется корректность отображения экрана.
""")
def test_full_onboarding_swipe_navigation(pages, logger):
    """Полная проверка навигации по онбордингу свайпами"""
    try:
        onboarding = pages.onboarding.swipes
        total_screens = 4  # Общее количество экранов онбординга
        logger.info("=== Начало теста: полная проверка свайпов онбординга ===")

        # Проход вперед через все экраны
        with allure.step("1. Проход вперед через все экраны (1 → 4)"):
            for screen_num in range(2, total_screens + 1):
                with allure.step(f"1.{screen_num-1}. Переход на экран {screen_num}"):
                    logger.debug(f"Свайп вперед на экран {screen_num}")
                    assert onboarding.swipe_forward_to_screen(screen_num), f"Не удалось перейти на экран {screen_num}"
                    logger.info(f"Успешно перешли на экран {screen_num}")

        # Проход назад через все экраны
        with allure.step("2. Проход назад через все экраны (4 → 1)"):
            for screen_num in range(total_screens - 1, 0, -1):
                with allure.step(f"2.{total_screens - screen_num}. Возврат на экран {screen_num}"):
                    logger.debug(f"Свайп назад на экран {screen_num}")
                    assert onboarding.swipe_backward_to_screen(screen_num), \
                        f"Не удалось вернуться на экран {screen_num}"
                    logger.info(f"Успешно вернулись на экран {screen_num}")

        logger.info("=== Тест успешно завершен: все свайпы работают корректно ===")

    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        allure.attach(
            name="Ошибка при выполнении теста",
            body=str(e),
            attachment_type=allure.attachment_type.TEXT
        )
        raise
