import pytest
import allure

@pytest.mark.onboarding
@pytest.mark.smoke
@allure.description("""
**Сценарий:** Проверка работы с языками в процессе онбординга.

**Шаги:**
1. Начальный экран: проверка кнопки 'Add or edit languages'.
2. Экран выбора языков: проверка кнопки 'Add language'.
3. Двойной возврат через системную навигацию.
4. Финальная проверка возврата на стартовый экран.

**Ожидаемый результат:**
- Все кнопки отображаются и кликабельны.
- Навигация возвращает пользователя на предыдущие экраны без ошибок.
""")
def test_add_or_edit_languages(pages, logger):
    """Тест кнопки 'Add or edit languages' и навигации обратно"""
    try:
        onboarding = pages.onboarding
        logger.info("=== Начало теста: проверка кнопки 'Add or edit languages' ===")
        with allure.step("1. Проверка начального экрана"):
            logger.debug("Проверяем видимость кнопки 'Add or edit languages'")
            assert onboarding.buttons.is_add_language_button_visible(), "Кнопка не отображается"
            onboarding.buttons.tap_add_language_button()
            logger.info("Кнопка 'Add or edit languages' найдена и нажата")

        with allure.step("2. Проверка экрана выбора языков"):
            logger.debug("Ищем кнопку 'Add language' в списке")
            assert onboarding.buttons.is_add_language_in_list_visible(), "Кнопка в списке не найдена"
            logger.info("Находимся на следующем экране после онбординга")
            onboarding.buttons.tap_add_language_in_list()
            logger.info("Кнопка 'Add language' найдена и нажата")

        with allure.step("3. Возврат через навигацию"):
            logger.debug("Проверяем кнопку 'Navigate up'")
            assert onboarding.buttons.is_navigate_up_visible(), "Кнопка навигации не найдена"
            logger.info("Находимся на экране добавления языка")
            onboarding.buttons.tap_navigate_up()
            logger.info("Кнопка 'Navigate up' найдена и нажата")

        with allure.step("4. Возврат через навигацию"):
            logger.debug("Проверяем кнопку 'Navigate up'")
            assert onboarding.buttons.is_navigate_up_visible(), "Кнопка навигации не найдена"
            logger.info("Вернулись на следующий после онбординга экран")
            onboarding.buttons.tap_navigate_up()
            logger.info("Кнопка 'Navigate up' найдена и нажата")

        with allure.step("5. Финальная проверка"):
            logger.debug("Проверяем, что вернулись на экран онбординга")
            assert onboarding.buttons.is_continue_button_visible(), "Не вернулись на экран онбординга"
            logger.info("Вернулись на экран онбординга")
        logger.info("=== Тест успешно завершен ===")

    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.onboarding
@pytest.mark.smoke
@allure.description("""
**Smoke-тест онбординга:**
1. Последовательно проверяет все 3 экрана:
   - Кнопка 'Continue' должна быть видима.
   - Нажатие приводит к переходу дальше.
2. Финальный экран:
   - Должна отображаться кнопка 'Get Started'.
Логируется номер текущего экрана при ошибках.
""")
def test_continue_through_all_screens(pages, logger):
    """Тестирование кнопки 'Continue' на всех экранах онбординга"""
    try:
        onboarding = pages.onboarding
        logger.info("=== Начало теста: проход по всем экранам онбординга ===")

        for i in range(3):
            with allure.step(f"{i + 1}. Экран {i + 1}"):
                logger.debug(f"Проверяем кнопку 'Continue' на экране {i + 1}")
                assert onboarding.buttons.is_continue_button_visible(), f"Кнопка не найдена на экране {i + 1}"
                logger.info(f"Кнопка 'Continue' найдена на экране {i + 1}")
                onboarding.buttons.tap_continue()
                logger.info(f"Кнопка 'Continue' нажата на экране {i + 1}")

        with allure.step("4. Проверка финального экрана"):
            logger.debug("Проверяем кнопку 'Get Started'")
            assert onboarding.buttons.is_get_started_visible(), "Кнопка 'Get Started' не найдена"
            logger.info("Все экраны пройдены успешно")

        logger.info("=== Тест успешно завершен ===")

    except Exception as e:
        logger.error(f"!!! Тест упал на экране {i + 1}: {str(e)}")
        raise

@pytest.mark.onboarding
@pytest.mark.smoke
@allure.description("""
Smoke-тест финального этапа онбординга:
- Логирует пропуск каждого из 3 экранов.
- Валидирует отображение и функциональность 'Get Started'.
- Проверяет переход на главный экран.
""")
def test_get_started_button(pages, logger):
    """Тестирование кнопки 'Get Started' на последнем экране онбординга"""
    try:
        onboarding = pages.onboarding
        logger.info("=== Начало теста: проверка кнопки 'Get Started' ===")

        with allure.step("1. Пропуск первых экранов"):
            for i in range(3):
                logger.debug(f"Пропускаем экран {i + 1}")
                assert onboarding.buttons.is_continue_button_visible(), f"Не удалось найти кнопку 'Continue' на экране {i + 1}"
                onboarding.buttons.tap_continue()
            logger.info("Успешно пропущены 3 экрана онбординга")

        with allure.step("2. Проверка кнопки 'Get Started'"):
            logger.debug("Ищем кнопку завершения онбординга")
            assert onboarding.buttons.is_get_started_visible(), "Кнопка 'Get Started' не найдена"
            onboarding.buttons.tap_get_started()
            logger.info("Кнопка 'Get Started' найдена и нажата")

        with allure.step("3. Проверка главного экрана"):
            logger.debug("Проверяем отображение главного экрана")
            assert onboarding.buttons.is_main_screen_visible(), "Главный экран не отобразился"
            logger.info("Успешный переход на главный экран")

        logger.info("=== Тест успешно завершен ===")

    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        raise

@pytest.mark.onboarding
@pytest.mark.smoke
@pytest.mark.parametrize("screen_count", [0, 1, 2])
@allure.description("""
Параметризованный тест проверки кнопки 'Skip' на разных экранах онбординга.
Проверяет:
1. Возможность пропустить онбординг с каждого из экранов (0-2)
2. Корректность перехода на главный экран после нажатия 'Skip'
""")
def test_skip_button_on_screens(pages, screen_count, logger):
    """Проверка кнопки 'Skip' на разных экранах онбординга"""
    try:
        onboarding = pages.onboarding
        logger.info(f"=== Начало теста: проверка кнопки 'Skip' (экран {screen_count + 1}) ===")

        with allure.step("1. Навигация до целевого экрана"):
            for i in range(screen_count):
                logger.debug(f"Переход через экран {i + 1}")
                assert onboarding.buttons.is_continue_button_visible(), f"Не удалось найти кнопку Continue на экране {i + 1}"
                onboarding.buttons.tap_continue()
            logger.info(f"Успешно достигнут экран {screen_count + 1}")

        with allure.step("2. Проверка кнопки 'Skip'"):
            logger.debug("Ищем кнопку пропуска онбординга")
            assert onboarding.buttons.is_skip_button_visible(), "Кнопка 'Skip' не найдена"
            onboarding.buttons.tap_skip()
            logger.info("Кнопка найдена и нажата")

        with allure.step("3. Проверка главного экрана"):
            logger.debug("Проверяем отображение главного экрана")
            assert onboarding.buttons.is_main_screen_visible(), "Главный экран не отобразился"
            logger.info("Успешный переход на главный экран")

        logger.info("=== Тест успешно завершен ===")

    except Exception as e:
        logger.error(f"!!! Тест упал на экране {screen_count + 1}: {str(e)}")
        raise