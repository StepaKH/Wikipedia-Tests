from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="/run_tests"), KeyboardButton(text="/stop_tests")],
            [KeyboardButton(text="/last_report"), KeyboardButton(text="/markers")],
            [KeyboardButton(text="/schedule_tests 22:30"), KeyboardButton(text="/cancel_schedule")],
            [KeyboardButton(text="/simulate_push")],
            [KeyboardButton(text="/help")]
        ],
        resize_keyboard=True
    )
    return keyboard
