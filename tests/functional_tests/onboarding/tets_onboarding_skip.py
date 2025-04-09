import pytest

@pytest.mark.parametrize("screen_count", [0, 1, 2])
def test_skip_button_on_screens(onboarding, screen_count):
    """Проверка кнопки 'Skip' на 1, 2 и 3 экранах онбординга"""

    for _ in range(screen_count):
        assert onboarding.is_continue_button_visible(), "Кнопка 'Continue' не отображается"
        onboarding.tap_continue()

    assert onboarding.is_skip_button_visible(), f"Кнопка 'Skip' не отображается на экране {screen_count + 1}"
    onboarding.tap_skip()

    assert onboarding.is_main_screen_visible(), "Главный экран не отображается после нажатия 'Skip'"