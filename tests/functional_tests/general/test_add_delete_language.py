import pytest
import allure
from paths import open_language_edit_screen

@pytest.mark.language
@pytest.mark.smoke
@allure.description("Тест: рандомное добавление языка")
def test_random_add_language(open_language_edit_screen, logger):
    """Тест на случайное добавление языка из списка"""
    try:
        lang_actions = open_language_edit_screen
        logger.info("=== Тест: рандомное добавление языка ===")

        with allure.step("1. Открываем экран добавления языка"):
            logger.debug("Проверяем видимость кнопки 'Add languages'")
            assert lang_actions.clicks.safe_click(lang_actions.ADD_LANGUAGE_TITLE)
            logger.info("Кнопка 'Add languages' найдена и нажата")

        with allure.step("2. Выбор случайного языка из списка"):
            logger.debug("Выбираем случайный язык из списка")
            added_language = lang_actions.choose_random_language()
            assert added_language is not None, "❌ Не удалось выбрать язык из списка"
            logger.info(f"Случайный язык выбран: {added_language}")

        with allure.step("3. Проверка, что язык отображается в списке"):
            logger.debug(f"Проверяем видимость языка '{added_language}' в списке")
            assert lang_actions.clicks.is_visible(lang_actions.language_by_name(added_language)), \
                f"Язык '{added_language}' не отображается в списке"
            logger.info(f"Язык '{added_language}' успешно отображается в списке")

        logger.info("=== Тест завершен: Язык успешно добавлен и отображается ===")

    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        allure.attach(
            name="Ошибка при выполнении теста",
            body=str(e),
            attachment_type=allure.attachment_type.TEXT
        )
        raise

@pytest.mark.language
@pytest.mark.smoke
@allure.description("Тест: добавление языка через поиск")
def test_add_language(open_language_edit_screen, logger, language_to_add=None):
    """
    Тест на добавление нового языка через поиск
    """
    try:
        lang_actions = open_language_edit_screen

        with allure.step("Открываем экран добавления языка"):
            logger.debug("Проверяем видимость кнопки 'Add languages'")
            assert lang_actions.clicks.safe_click(lang_actions.ADD_LANGUAGE_TITLE)
            logger.info("Кнопка 'Add languages' найдена и нажата")

        if language_to_add is None:
            with allure.step("Выбираем случайный язык для поиска"):
                logger.debug("Выбираем случайный язык из списка")
                language_to_add = lang_actions.choose_random_language(max_scrolls=3, click_fact=None)
                assert language_to_add is not None, "❌ Не удалось выбрать язык из списка"
                logger.info(f"Случайный язык выбран для поиска: {language_to_add}")

        with allure.step("Добавление языка через поиск"):
            logger.debug(f"Ищем язык '{language_to_add}' через поиск")
            added = lang_actions.add_language_via_search(language_to_add)
            assert added, "❌ Не удалось добавить язык через поиск"
            logger.info(f"Язык '{language_to_add}' успешно добавлен через поиск")

        with allure.step("Проверка, что язык отображается в списке"):
            logger.debug(f"Проверяем видимость языка '{language_to_add}' в списке")
            assert lang_actions.clicks.is_visible(lang_actions.language_by_name(language_to_add)), \
                f"Язык '{language_to_add}' не отображается в списке"
            logger.info(f"Язык '{language_to_add}' успешно отображается в списке")

        logger.info("=== Тест успешно завершен: язык успешно добавлен и отображается ===")

    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        allure.attach(
            name="Ошибка при выполнении теста",
            body=str(e),
            attachment_type=allure.attachment_type.TEXT
        )
        raise

@pytest.mark.language
@pytest.mark.smoke
@allure.description("Тест проверяет корректность перемещения языка в конец списка с помощью drag-and-drop.")
def test_drag_language_to_bottom(open_language_edit_screen, logger, new_language=None):
    """Тест на перемещение языка в конец списка"""
    try:
        lang_page = open_language_edit_screen
        logger.info("=== Тест: перемещение языка вниз списка ===")

        if not new_language:
            assert lang_page.clicks.safe_click(lang_page.ADD_LANGUAGE_TITLE)
            lang_page.add_language_via_search('Русский')

        with allure.step("Получаем текущий список языков"):
            logger.debug("Получаем список отображаемых языков")
            languages = lang_page.get_language_names()
            assert languages, "❌ Список языков пуст"

            logger.debug("Проверка на необходимое количество языков в списке для перемещения")
            assert len(languages) >= 3, 'Недостаточно языков для перемещения'

            logger.info(f"Текущий список языков: {languages[:-1]}")

        with allure.step("Перемещаем первый язык в конец списка"):
            language_to_move = languages[0]
            logger.debug(f"Пробуем переместить язык '{language_to_move}' вниз списка")
            result = lang_page.move_language_to_bottom(language_to_move, new_language=new_language)
            assert result, f"❌ Не удалось переместить язык '{language_to_move}' вниз"
            logger.info(f"✅ Язык '{language_to_move}' успешно перемещён вниз")

        with allure.step("Проверка, что язык оказался внизу"):
            updated_languages = lang_page.get_language_names()
            assert updated_languages[-2] == language_to_move, \
                f"❌ Язык '{language_to_move}' не оказался внизу (ожидался на последней позиции)"
            logger.info(f"🎯 Язык '{language_to_move}' теперь находится внизу списка: {updated_languages[:-1]}")

        logger.info("=== Тест успешно завершён: язык перемещён ===")

    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        allure.attach(
            name="Ошибка теста",
            body=str(e),
            attachment_type=allure.attachment_type.TEXT
        )
        raise

@pytest.mark.language
@pytest.mark.smoke
@allure.description("Тест проверяет корректность перемещения языка в конец списка с помощью drag-and-drop после добавления нового языка в список.")
def test_drag_language_after_add(open_language_edit_screen, logger):
    try:
        logger.info("=== Тест: перемещение языка вниз списка после добавления нового===")

        test_random_add_language(open_language_edit_screen, logger)

        test_drag_language_to_bottom(open_language_edit_screen, logger, new_language=True)

    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        allure.attach(
            name="Ошибка теста",
            body=str(e),
            attachment_type=allure.attachment_type.TEXT
        )
        raise

@pytest.mark.language
@pytest.mark.smoke
@allure.description("Тест проверяет повторное добавление одного и того же языка через поле поиска.")
def test_re_adding_language_search_bar(open_language_edit_screen, logger):
    try:
        lang_actions = open_language_edit_screen
        logger.info("=== Тест: повторное добавление языка через строку поиска===")

        with allure.step("Выбираем случайный язык для поиска"):
            logger.debug("Проверяем видимость кнопки 'Add languages'")
            assert lang_actions.clicks.safe_click(lang_actions.ADD_LANGUAGE_TITLE)
            logger.info("Кнопка 'Add languages' найдена и нажата")

            logger.debug("Выбираем случайный язык из списка")
            language_to_add = lang_actions.choose_random_language(max_scrolls=3, click_fact=None)
            assert language_to_add is not None, "❌ Не удалось выбрать язык из списка"
            logger.info(f"Случайный язык выбран для поиска: {language_to_add}")

        lang_actions.clicks.safe_click(lang_actions.BACK_BTN)
        test_add_language(open_language_edit_screen, logger, language_to_add)
        test_add_language(open_language_edit_screen, logger, language_to_add)

    except Exception as e:
        logger.error(f"!!! Тест упал с ошибкой: {str(e)}")
        allure.attach(
            name="Ошибка теста",
            body=str(e),
            attachment_type=allure.attachment_type.TEXT
        )
        raise

@pytest.mark.language
@pytest.mark.smoke
@allure.description("Удаление случайного языка через долгое нажатие")
def test_delete_random_language_by_long_press(open_language_edit_screen, logger):
    try:
        lang_page = open_language_edit_screen
        logger.info("=== Тест: удаление случайного языка через долгое нажатие ===")

        assert lang_page.clicks.safe_click(lang_page.ADD_LANGUAGE_TITLE)
        lang_page.add_language_via_search('Русский')

        with allure.step("Удаляем язык через long press"):
            deleted = lang_page.remove_random_language_by_long_press()
            assert deleted, "❌ Не удалось удалить язык через долгое нажатие"

        with allure.step("Проверка, что язык удалён"):
            updated_languages = lang_page.get_language_names()
            assert deleted not in updated_languages, \
                f"❌ Язык '{deleted}' всё ещё присутствует в списке после удаления"
            logger.info(f"✅ Язык '{deleted}' больше не отображается в списке")

    except Exception as e:
        logger.error(f"!!! Ошибка: {e}")
        allure.attach(name="Ошибка", body=str(e), attachment_type=allure.attachment_type.TEXT)
        raise

@pytest.mark.language
@pytest.mark.smoke
@allure.description("Удаление случайного языка через меню")
def test_delete_random_language_via_menu(open_language_edit_screen, logger):
    try:
        lang_page = open_language_edit_screen
        logger.info("=== Тест: удаление случайного языка через меню ===")

        assert lang_page.clicks.safe_click(lang_page.ADD_LANGUAGE_TITLE)
        lang_page.add_language_via_search('Русский')

        with allure.step("Удаляем язык через меню"):
            deleted = lang_page.remove_random_language_via_menu()
            assert deleted, "❌ Не удалось удалить язык через меню"

        with allure.step("Проверка, что язык удалён"):
            updated_languages = lang_page.get_language_names()
            assert deleted not in updated_languages, \
                f"❌ Язык '{deleted}' всё ещё присутствует в списке после удаления"
            logger.info(f"✅ Язык '{deleted}' больше не отображается в списке")

    except Exception as e:
        logger.error(f"!!! Ошибка: {e}")
        allure.attach(name="Ошибка", body=str(e), attachment_type=allure.attachment_type.TEXT)
        raise