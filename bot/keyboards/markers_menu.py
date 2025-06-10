from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ALLOWED_MARKERS = ["smoke", "negative", "onboarding", "positive", "auth", "registration", "validation", "customize_feed", "customize_random", "article", "tabs", "search", "saved"]

def get_marker_menu() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text=m, callback_data=f"marker_{m}")]
        for m in ALLOWED_MARKERS
    ]
    buttons.append([InlineKeyboardButton(text="⏭ Пропустить", callback_data="skip_marker")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)
