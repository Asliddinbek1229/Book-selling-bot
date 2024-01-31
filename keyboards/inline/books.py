from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

books_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Masala kitobi 1-qism (Genetikagacha)", callback_data='part_1')
        ],
        [
            InlineKeyboardButton(text="Masala kitobi 2-qism (Genetika, ozuqa zanjiri)", callback_data='part_2')
        ],
    ],
)

pay_book = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💳Sotib olish", callback_data='pay')
        ],
    ],
)

check_pay = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ha", callback_data='yes'),
            InlineKeyboardButton(text="Yo'q", callback_data='no')
        ],
    ],
)