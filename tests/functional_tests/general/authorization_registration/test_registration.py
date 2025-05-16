import pytest
import allure
from tests.functional_tests.general.paths import open_log_in_screen

@pytest.mark.registration
@pytest.mark.negative
@allure.description('Проверка валидации username при регистрации: существующее имя пользователя')
def test_username_already_exists(open_log_in_screen, logger):
    try:
        page = open_log_in_screen
        logger.info("=== Тест: проверка существующего username ===")
        existing_username = "Stepa"

        with allure.step("1. Заполняем форму с существующим username"):
            page.fill_registration_form(username=existing_username)
            allure.attach(
                name="Введенные данные",
                body=f"Username: {existing_username}",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("2. Проверяем отображение ошибки"):
            assert page.clicks.is_visible(page.ERROR_CODE), "❌ Сообщение об ошибке не отобразилось"
            logger.info(f"✅ Ошибка отображается для существующего username: '{existing_username}'")

        with allure.step("3. Проверяем блокировку продолжения регистрации"):
            assert not page.clicks.click(page.CONTINUE_BUTTOM), "❌ Удалось продолжить с существующим username"
            logger.info("✅ Кнопка продолжения заблокирована")

    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        allure.attach(
            name="Ошибка при выполнении теста",
            body=str(e),
            attachment_type=allure.attachment_type.TEXT
        )
        raise

@pytest.mark.registration
@pytest.mark.validation
@pytest.mark.parametrize("password", ["1234567", "pass", "1"],
                         ids=["7 symbols", "4 symbols", "1 symbol"])
@allure.description('Проверка валидации пароля при регистрации: слишком короткий пароль')
def test_password_too_short(open_log_in_screen, logger, password):
    try:
        page = open_log_in_screen
        username = "StepaKH"
        logger.info(f"=== Тест: проверка короткого пароля ({len(password)} символов) ===")

        with allure.step("1. Заполняем форму с коротким паролем"):
            page.fill_registration_form(username=username, password=password)
            allure.attach(
                name="Введенные данные",
                body=f"Username: {username}\nPassword: {password}",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("2. Пытаемся продолжить регистрацию"):
            assert page.clicks.safe_click(page.CONTINUE_BUTTOM), "❌ Кнопка 'Продолжить' не найдена"

        with allure.step("3. Проверяем отображение ошибки"):
            assert page.clicks.is_visible(page.ERROR_CODE), "❌ Сообщение об ошибке не отобразилось"
            logger.info(f"✅ Ошибка отображается")

    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        allure.attach(
            name="Ошибка при выполнении теста",
            body=str(e),
            attachment_type=allure.attachment_type.TEXT
        )
        raise

@pytest.mark.registration
@pytest.mark.negative
@allure.description('Проверка валидации пароля при регистрации: несовпадающие пароли')
def test_repeat_password_mismatch(open_log_in_screen, logger):
    try:
        page = open_log_in_screen
        logger.info("=== Тест: проверка несовпадающих паролей ===")

        username = "StepaKH"
        password = "Pass12345"
        wrong_password = password + "1"

        with allure.step("1. Заполняем форму с разными паролями"):
            page.fill_registration_form(
                username=username,
                password=password,
                repeat_password=wrong_password
            )
            allure.attach(
                name="Введенные данные",
                body=f"Password: {password}\nRepeat password: {wrong_password}",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("2. Пытаемся продолжить регистрацию"):
            assert page.clicks.safe_click(page.CONTINUE_BUTTOM), "❌ Кнопка 'Продолжить' не найдена"

        with allure.step("3. Проверяем отображение ошибки"):
            assert page.clicks.is_visible(page.ERROR_CODE), "❌ Сообщение об ошибке не отобразилось"
            logger.info(f"✅ Ошибка отображается")

    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        allure.attach(
            name="Ошибка при выполнении теста",
            body=str(e),
            attachment_type=allure.attachment_type.TEXT
        )
        raise

@pytest.mark.registration
@pytest.mark.validation
@allure.description('Проверка валидации email при регистрации: некорректные форматы email')
@pytest.mark.parametrize("email, test_case", [
    pytest.param("without.at.sign", "Missing @ symbol",
                 id="email_no_at_symbol"),
    pytest.param("missing@domain", "Missing domain part",
                 id="email_no_domain"),
    pytest.param("@missing.local.part", "Missing local part",
                 id="email_no_local_part"),
    pytest.param("space in@email.com", "Contains spaces",
                 id="email_with_spaces"),
    pytest.param("invalid@.com", "Dot after @",
                 id="email_dot_after_at"),
    pytest.param("invalid@domain..com", "Consecutive dots",
                 id="email_consecutive_dots"),
    pytest.param("invalid@domain.c", "Short domain",
                 id="email_short_domain"),
    pytest.param("no-tld@domain", "No top-level domain",
                 id="email_no_tld"),
    pytest.param("special^chars@example.com", "Invalid characters",
                 id="email_invalid_chars"),
    pytest.param("кириллица@домен.рф", "Cyrillic characters",
                 id="email_cyrillic"),
    pytest.param("too.long." * 10 + "@example.com", "Too long email",
                 id="email_too_long"),
    pytest.param("valid@but.with.space.at.end ", "Trailing space",
                 id="email_trailing_space"),
    pytest.param(" valid@but.with.space.at.start", "Leading space",
                 id="email_leading_space"),
])
def test_invalid_email_validation(open_log_in_screen, logger, email, test_case):
    try:
        page = open_log_in_screen
        logger.info(f"=== Тест: проверка невалидного email ({test_case}) ===")

        with allure.step("1. Подготавливаем тестовые данные"):
            username = "StepaKH"
            password = "Pass12345"
            allure.attach(
                name="Тестовые данные",
                body=f"Username: {username}\nEmail: {email}\nPassword: {password}",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("2. Заполняем форму регистрации с некорректным email"):
            page.fill_registration_form(
                username=username,
                email=email,
                password=password,
                repeat_password=password
            )

        with allure.step("3. Пытаемся продолжить регистрацию"):
            assert page.clicks.safe_click(page.CONTINUE_BUTTOM), "❌ Кнопка 'Продолжить' не найдена или недоступна"
            logger.debug("Кнопка 'Продолжить' нажата успешно")

        with allure.step("4. Проверяем отображение ошибки валидации"):
            assert page.clicks.is_visible(page.ERROR_CODE), f"❌ Ошибка не отобразилась для email: {email}"
            logger.info(f"✅ Отображается ошибка")

    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        allure.attach(
            name="Ошибка при выполнении теста",
            body=str(e),
            attachment_type=allure.attachment_type.TEXT
        )
        raise

@pytest.mark.registration
@pytest.mark.smoke
@allure.description("Проверка поведения при регистрации без email")
def test_registration_without_email(open_log_in_screen, logger):
    """Проверка сценария, когда пользователь не указывает email"""
    try:
        page = open_log_in_screen

        with allure.step("1. Заполняем форму регистрации без email"):
            test_username = "StepaKH"
            page.fill_registration_form(
                username=test_username,
                password="ValidPass123",
                repeat_password="ValidPass123",
                email=""  # Пустое поле email
            )
            allure.attach(
                name="Введенные данные",
                body=f"Логин: {test_username}\nEmail: [не указан]",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("2. Нажимаем кнопку продолжения"):
            assert page.clicks.safe_click(page.CONTINUE_BUTTOM), "Кнопка 'Продолжить' не найдена"

        with allure.step("3. Проверяем появление диалогового окна"):
            assert page.clicks.is_visible(page.EMAIL_WARNING_DIALOG), "Диалоговое окно не появилось"

        with allure.step("4. Проверяем кнопку 'Продолжить без email'"):
            assert page.clicks.safe_click(page.CONTINUE_WITHOUT_EMAIL_BTN), "Кнопка 'Продолжить без email' не найдена"
            assert page.clicks.is_visible(page.CAPTCHA_SUBMIT_BTN), "Не перешли на экран с капчей"
            logger.info("✅ Успешный переход после 'Продолжить без email'")

            # Возвращаемся назад для проверки второй кнопки
            page.clicks.safe_click(page.BACK_BTN)

        with allure.step("5. Нажимаем кнопку продолжения"):
            assert page.clicks.safe_click(page.CONTINUE_BUTTOM), "Кнопка 'Продолжить' не найдена"

        with allure.step("6. Проверяем кнопку 'Ввести email'"):
            assert page.clicks.safe_click(page.ENTER_EMAIL_BTN), "Кнопка 'Ввести email' не найдена"
            assert page.clicks.is_visible(page.JOIN_WIKIPEDIA_SCREEN), "Не вернулись на экран ввода email"
            logger.info("✅ Успешный переход после 'Ввести email'")

    except Exception as e:
        logger.error(f"Ошибка в тесте: {str(e)}")
        allure.attach(
            name="Ошибка",
            body=str(e),
            attachment_type=allure.attachment_type.TEXT
        )
        raise

@pytest.mark.registration
@pytest.mark.positive
@allure.description("Проверка успешной регистрации с валидными данными")
def test_successful_registration(open_log_in_screen, logger):
    """Проверка полного сценария успешной регистрации"""
    try:
        page = open_log_in_screen

        with allure.step("1. Заполняем форму валидными данными"):
            test_username = "StepaKH"
            test_email = "stepa@gmail.com"
            page.fill_registration_form(
                username=test_username,
                email=test_email,
                password="ValidPass123",
                repeat_password="ValidPass123"
            )
            allure.attach(
                name="Введенные данные",
                body=f"Логин: {test_username}\nEmail: {test_email}",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("2. Нажимаем кнопку продолжения"):
            assert page.clicks.safe_click(page.CONTINUE_BUTTOM), "Кнопка 'Продолжить' не найдена"

        with allure.step("3. Проверяем переход на экран с капчей"):
            assert page.clicks.is_visible(page.CAPTCHA_SUBMIT_BTN), "Не перешли на экран с капчей"
            logger.info("✅ Успешный переход на экран с капчей")

    except Exception as e:
        logger.error(f"Ошибка в тесте: {str(e)}")
        allure.attach(
            name="Ошибка",
            body=str(e),
            attachment_type=allure.attachment_type.TEXT
        )
        raise