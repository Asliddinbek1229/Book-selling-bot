from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuKeybord = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="👁Kitoblarni ko'rish"),
            KeyboardButton(text="👨‍💻Admin bilan aloqa")
        ],
    ],
)