from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menuKeybords import menuKeybord

from loader import dp, bot

feruza = {}


@dp.message_handler(CommandStart(deep_link='Feruza_Jumayeva'), state='*')
async def bot_start(messaga: types.Message):
    feruza[messaga.from_user.full_name] = messaga.from_user.id
    args = messaga.get_args()
    text = f"Salom <b>{messaga.from_user.full_name}</b>. Xush kelibsiz. \n"
    text += f"Sizni <b>{args}</b> tavsiya qildi."
    await bot.send_message(chat_id=634448116, text=f"Xurmatli Feruza Jumayeva\n<b>{messaga.from_user.full_name}</b> ismli foydalanuvchi sizning linkingiz orqali botga qo'shildi.")
    await messaga.answer(text, reply_markup=menuKeybord)
    await bot.send_message(chat_id=982935447, text=feruza)

@dp.message_handler(CommandStart(deep_link='BioMaqsad'), state='*')
async def bot_start(messaga: types.Message):
    args = messaga.get_args()
    text = f"Salom <b>{messaga.from_user.full_name}</b>. Xush kelibsiz. \n"
    text += f"Siz <b>{args}</b> kanali orqali botga qo'shildingiz."
    await bot.send_message(chat_id=982935447, text=f"<b>{messaga.from_user.full_name}</b> biomaqsad kanali orqali botga qo'shildi.")
    await messaga.answer(text, reply_markup=menuKeybord)

@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    await message.answer(f"👋 Salom, <b>{message.from_user.full_name}!</b>\n\nQuyidagi menulardan birini tanlang 👇", reply_markup=menuKeybord)
    await bot.send_message(chat_id=982935447, text=f"{message.from_user.full_name} ismli user qaydandur botga start bosdi.")
