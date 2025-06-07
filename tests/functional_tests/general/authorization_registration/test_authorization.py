import pytest
import allure
from tests.functional_tests.general.paths import open_log_in_screen

@pytest.mark.auth
@pytest.mark.smoke
@allure.description('Проверка работы всех кнопок внутри экрана "Log in / join Wikipedia"')
def test_auth_bottoms(open_log_in_screen, logger):
    try:
        login_page = open_log_in_screen
        logger.info("=== Тест: проверка всех кнопок ===")

        with allure.step("1. Проверка работы кнопки 'Log in'"):
            login_page.go_to_login_screen()

        with allure.step("2. Кнопка 'Join Wikipedia'"):
            logger.debug("Нажимаем на кнопку 'Join Wikipedia'")
            assert login_page.clicks.safe_click(
                login_page.JOIN_WIKIPEDIA_BUTTOM), "❌ Кнопка 'Join Wikipedia' не найдена"
            assert login_page.clicks.is_visible(
                login_page.JOIN_WIKIPEDIA_SCREEN), "❌ Не перешли на экран 'Join Wikipedia'"
            logger.info("✅ Перешли на экран 'Join Wikipedia'")

        with allure.step("3. Кнопка 'Назад' с экрана авторизации"):
            login_page.go_to_login_screen()

            logger.debug("Нажимаем на кнопку 'Назад'")
            assert login_page.clicks.safe_click(login_page.BACK_BTN), "❌ Кнопка 'Назад' не найдена"
            assert login_page.clicks.is_visible(login_page.MAIN_SCREEN), "❌ Не вернулись на главный экран"
            logger.info("✅ Возврат с экрана 'Log in' прошел успешно")

        with allure.step("4. Кнопка 'Назад' с экрана регистрации"):
            logger.debug("Переход в меню -> Log in / join Wikipedia")
            assert login_page.clicks.safe_click(login_page.MENU_BUTTOM), "❌ Кнопка 'Меню' не найдена"
            assert login_page.clicks.safe_click(login_page.MAIN_LOGIN_BUTTOM), "❌ Кнопка перехода не найдена"
            logger.debug("Нажимаем кнопку 'Назад'")
            assert login_page.clicks.safe_click(login_page.BACK_BTN), "❌ Кнопка 'Назад' не найдена"
            assert login_page.clicks.is_visible(login_page.MAIN_SCREEN), "❌ Не вернулись на главный экран"
            logger.info("✅ Возврат с экрана 'Join Wikipedia' прошел успешно")

    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        allure.attach(
            name="Ошибка при выполнении теста",
            body=str(e),
            attachment_type=allure.attachment_type.TEXT
        )
        raise

@pytest.mark.auth
@pytest.mark.smoke
@allure.description('Проверка свайпов с экранов Log in и Join Wikipedia')
def test_auth_swipes(open_log_in_screen, logger):
    try:
        login_page = open_log_in_screen
        logger.info("=== Тест: проверка всех свайпов ===")

        with allure.step("1. Свайпы с экрана Join Wikipedia"):
            login_page.go_to_main_screen(direction="left", from_screen=login_page.JOIN_WIKIPEDIA_SCREEN)
            logger.debug("Переход в меню -> Log in / join Wikipedia")
            assert login_page.clicks.safe_click(login_page.MENU_BUTTOM)
            assert login_page.clicks.safe_click(login_page.MAIN_LOGIN_BUTTOM)
            login_page.go_to_main_screen(direction="right", from_screen=login_page.JOIN_WIKIPEDIA_SCREEN)

        with allure.step("2. Свайпы с экрана Log in"):
            for direction in ["right", "left"]:
                logger.debug("Переход в меню -> Log in / join Wikipedia")
                assert login_page.clicks.safe_click(login_page.MENU_BUTTOM)
                assert login_page.clicks.safe_click(login_page.MAIN_LOGIN_BUTTOM)
                login_page.go_to_login_screen()
                login_page.go_to_main_screen(direction=direction, from_screen=login_page.LOGIN_SCREEN)

    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        allure.attach(
            name="Ошибка при выполнении теста",
            body=str(e),
            attachment_type=allure.attachment_type.TEXT
        )
        raise

@pytest.mark.auth
@pytest.mark.negative
@allure.description("Проверка авторизации с неправильным логином")
def test_login_with_wrong_username(open_log_in_screen, logger):
    """Проверка авторизации с неверным именем пользователя"""
    try:
        page = open_log_in_screen
        page.go_to_login_screen()

        with allure.step("1. Заполняем форму неверным логином"):
            page.fill_auth_form(
                login="wrong_username",
                password="08.06.2005"
            )
            allure.attach(
                name="Введенные данные",
                body="Логин: wrong_username\nПароль: 08.06.2005",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("2. Нажимаем кнопку входа"):
            assert page.clicks.safe_click(page.LOGIN_BUTTON), "Кнопка входа не найдена"

        with allure.step("3. Проверяем сообщение об ошибке"):
            assert page.clicks.is_visible(page.ERROR_MESSAGE), "Сообщение об ошибке не появилось"
            logger.info(f"Получено сообщение об ошибке")

    except Exception as e:
        logger.error(f"Ошибка в тесте: {str(e)}")
        allure.attach(
            name="Ошибка",
            body=str(e),
            attachment_type=allure.attachment_type.TEXT
        )
        raise

@pytest.mark.auth
@pytest.mark.negative
@allure.description("Проверка авторизации с неправильным паролем")
def test_login_with_wrong_password(open_log_in_screen, logger):
    """Проверка авторизации с неверным паролем"""
    try:
        page = open_log_in_screen
        page.go_to_login_screen()

        with allure.step("1. Заполняем форму неверным паролем"):
            page.fill_auth_form(
                login="Artv1dal",
                password="wrong_password"
            )
            allure.attach(
                name="Введенные данные",
                body="Логин: correct_username\nПароль: wrong_password",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("2. Нажимаем кнопку входа"):
            assert page.clicks.safe_click(page.LOGIN_BUTTON), "Кнопка входа не найдена"

        with allure.step("3. Проверяем сообщение об ошибке"):
            assert page.clicks.is_visible(page.ERROR_MESSAGE), "Сообщение об ошибке не появилось"
            logger.info(f"Получено сообщение об ошибке")

    except Exception as e:
        logger.error(f"Ошибка в тесте: {str(e)}")
        allure.attach(
            name="Ошибка",
            body=str(e),
            attachment_type=allure.attachment_type.TEXT
        )
        raise

@pytest.mark.auth
@pytest.mark.positive
@allure.description("Проверка успешной авторизации")
def test_successful_login(open_log_in_screen, logger, log_out):
    """Проверка успешного сценария авторизации"""
    try:
        page = open_log_in_screen
        page.go_to_login_screen()

        with allure.step("1. Заполняем форму валидными данными"):
            page.fill_auth_form(
                login="Stepa2005",
                password="10.01.05"
            )
            allure.attach(
                name="Введенные данные",
                body=f"Логин: leviofan2005\nПароль: [скрыто]",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("2. Нажимаем кнопку входа"):
            assert page.clicks.safe_click(page.LOGIN_BUTTON), "Кнопка входа не найдена"

        with allure.step("3. Проверяем успешный вход"):
            main_screen = page.clicks.is_visible(page.MAIN_SCREEN)

            if not main_screen:
                success_login = page.clicks.is_visible(page.SUCCESS_LOGIN_INDICATOR)

                if not success_login:
                    logger.error("Не отобразился ни индикатор успешного входа, ни главный экран")
                    raise AssertionError("Не отобразился ни индикатор успешного входа, ни главный экран")

                with allure.step("4. Нажатие кнопки 'Dont allow'"):
                    assert page.clicks.safe_click(page.PERMISSION_DENY_BUTTON_BTN), "Кнопка 'Dont allow' не найдена"
                    logger.info("Кнопка 'Dont allow' найдена и нажата")

            logger.info("✅ Успешная авторизация (определен целевой экран)")

    except Exception as e:
        logger.error(f"Ошибка в тесте: {str(e)}")
        allure.attach(
            name="Ошибка",
            body=str(e),
            attachment_type=allure.attachment_type.TEXT
        )
        raise