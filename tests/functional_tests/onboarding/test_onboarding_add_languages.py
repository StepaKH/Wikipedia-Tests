def test_add_or_edit_languages(onboarding):
    """Тест кнопки 'Add or edit languages' и навигации обратно"""

    # Проверка кнопки 'Add or edit languages' на главном экране
    assert onboarding.is_add_language_button_visible(), "Кнопка 'Add or edit languages' не отображается"
    onboarding.tap_add_language_button()

    # Нажимаем кнопку "Add language" в списке
    assert onboarding.is_add_language_in_list_visible(), "Кнопка 'Add language' не отображается"
    onboarding.tap_add_language_in_list()

    # Появляется кнопка "Navigate up" — возвращаемся на экран выбора языка
    assert onboarding.is_navigate_up_visible(), "Кнопка 'Navigate up' не отображается (1-й раз)"
    onboarding.tap_navigate_up()

    # Возвращаемся на экран онбординга снова через "Navigate up"
    assert onboarding.is_navigate_up_visible(), "Кнопка 'Navigate up' не отображается (2-й раз)"
    onboarding.tap_navigate_up()

    # Проверка, что вернулись на экран с кнопкой "Continue"
    assert onboarding.is_continue_button_visible(), "Кнопка 'Continue' не отображается — возможно, не вернулись на экран онбординга"
