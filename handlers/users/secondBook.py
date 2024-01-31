from aiogram import types
from aiogram.types import CallbackQuery, InputFile
from aiogram.dispatcher import FSMContext
from loader import bot, dp
from aiogram.dispatcher.filters import Text

from states.pay import PayState, PayCheck

from keyboards.inline.books import books_menu, pay_book, check_pay

from handlers.users.start import feruza

@dp.callback_query_handler(text='part_2')
async def sec_book(call: CallbackQuery):
    await call.answer("Ikkinchi kitob tayyorlanmoqda.\n\nNasib etsa 10 kunda tayyor bo'ladi", show_alert=True)