def test_get_started_button(onboarding):
    """Тестирование кнопки 'Get Started' на последнем экране онбординга"""

    for _ in range(3):  # Пропускаем первые 3 экрана
        assert onboarding.is_continue_button_visible(), "Кнопка 'Continue' не отображается"
        onboarding.tap_continue()

    assert onboarding.is_get_started_visible(), "Кнопка 'Get Started' не отображается"
    onboarding.tap_get_started()

    assert onboarding.is_main_screen_visible(), "Главный экран не отображается после нажатия 'Get Started'"