import pytest

def test_continue_through_all_screens(onboarding):
    """Тестирование кнопки 'Continue' на всех экранах онбординга"""

    for _ in range(3):
        assert onboarding.is_continue_button_visible(), "Кнопка 'Continue' не отображается"
        onboarding.tap_continue()

    assert onboarding.is_get_started_visible(), "Кнопка 'Get Started' не отображается"