from aiogram import types
from aiogram.types import CallbackQuery, InputFile
from aiogram.dispatcher import FSMContext
from loader import bot, dp
from aiogram.dispatcher.filters import Text

from states.pay import PayState, PayCheck

from keyboards.inline.books import books_menu, pay_book, check_pay

from handlers.users.start import feruza


@dp.message_handler(Text("👁Kitoblarni ko'rish"), state='*')
async def book_show(msg: types.Message):
    await msg.delete()
    await msg.answer("Kitoblardan birini tanlang👇", reply_markup=books_menu)


@dp.callback_query_handler(text='part_1', state='*')
async def part_one(call: CallbackQuery, state: FSMContext):
    albums = types.MediaGroup()
    photo1 = InputFile(path_or_bytesio="Imagine/part1_1.jpg")
    photo2 = InputFile(path_or_bytesio="Imagine/part1_2.jpg")
    text = "Yangi <b>Masala kitobini</b> sizlarga taqdim etaman.\n\n"
    text += "<i>✅ Biologiyadagi 6 ta eng katta mavzular yuzasidan masalalar ishlash bo'yicha qo'llanmalar, metodikalar</i>\n"
    text += "<i>✅ Yechimli masalalar 141 ta (Masalalarning ishlanishi o'ta aniq, ipidan ignasigacha maydalab tushuntirilgan</i>\n"
    text += "<i>✅ Mustaqil ishlash uchun masalalar 708 ta (DTM, Attestatsiya va Milliy sertifikat darajasidagi masala va mashqlar)</i>\n"
    text += "<b>🧨 BONUS:</b> Kitobni xarid qilganlarga 141 ta masalalarni ishlanishi video tahlil holatida taqdim etiladi.\n\n"
    text += "<b>SHOSHILING❗️❗️❗️</b>\n"
    text += "🫡 Bu kitobni harid qilgan odam bizga to'lagan puliga albatda rozi bo'ladi. Agar rozi bo'lmasangiz to'lagan pulingiz 100% qaytarib beramiz. Ishonib aytaman kitob uyaltirib qo'ymaydi\n\n"
    text += "©Kitob mualliflik huquqiga ega. Endi kitobni pdf varianti ham sotuvda😍\n\n"
    text += "💰 PDF varianti <b>100 000</b> so'm\n\n"


    albums.attach_photo(photo=photo1)
    albums.attach_photo(photo=photo2, caption=text)

    await call.message.answer_media_group(media=albums)
    await call.message.answer("<b>Kitobni sotib olish uchun 'Sotib olish' tugmasini bosing👇.</b>", reply_markup=pay_book)
    await call.answer()
    await call.message.delete()


@dp.callback_query_handler(text='pay', state='*')
async def pay_boook(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(call.from_user.id, call.message.message_id-1)
    await bot.delete_message(call.from_user.id, call.message.message_id-2)
    await call.message.delete()
    text = "<b>❗️ ESLATMA</b>\nKitobni qo'lga kiritishingiz uchun to'lovni amalga oshirishingiz kerak!!!\n\n"
    text += "<b>Kitob narxi:</b> 100 000 so'm\n\n"
    text += "<code>8600140414140476</code>\n<i>Dagaraliyev Asliddinbek</i>\n\nTo'lovni ushbu kartaga qilasiz\n\n"
    text += "To'lovni amalga oshirganingizdan so'ng to'lov chekini botga yuboring.\n"
    text += "Shundan so'ng kitob sizga yuboriladi.\n\n\n"
    text += "<b>Iltimos botga to'lov chekini faqatgini 'Sotib olish' tugmasini bosgandan so'ng yuboring!!!</b>"
    await call.message.answer(text)

    user_id = call.from_user.id
    name = call.from_user.full_name

    users_f = []
    for k, v in feruza.items():
        users_f.append(v)
        if v == user_id:
            await bot.send_message(chat_id=634448116, text=f"Xurmatli Feruza Jumayeva. <b>{k}</b> ismli foydalanuvchi siz bergan link orqali <b>Asliddinbek</b>ning kitobini sotib olmoqchi.\n Agar sotib olsa, sizga xabar yuboramiz!")
            await bot.send_message(chat_id=982935447, text=f"<b>{k}</b> foydalnuvchi kitobni Feruza Jumayeva linki orqali sotib olmoqchi")
        # else:
        #     await bot.send_message(chat_id=982935447, text=f"<b>{name}</b> foydalnuvchi kitobni o'zimizni kanal orqali sotib olmoqchi")
    if not user_id in users_f:
        await bot.send_message(chat_id=982935447, text=f"<b>{name}</b> foydalnuvchi kitobni o'zimizni kanal orqali sotib olmoqchi")

    await PayState.firstState.set()

# --------------------------------------------------------------------------------------------------------------------------------------

@dp.message_handler(content_types='photo', state=PayState.firstState)
async def get_chek(msg: types.Message, state: FSMContext):
    # await bot.delete_message(msg.from_user.id, msg.message_id-1)
    # await bot.delete_message(msg.from_user.id, msg.message_id-2)
    check = msg.photo[-1].file_id
    user_id = msg.from_user.id
    name = msg.from_user.full_name

    await state.update_data(user_id=user_id)

    text = "To'lovingiz tekshirish uchun Adminga yuborildi. \n❗️❗️❗️Tekshirish biroz vaqt olishi mumkin\n\n<b>Iltimos biroz kuting</b>"
    await bot.send_photo(chat_id=982935447, photo=check)
    await bot.send_message(chat_id=982935447, text=f"<code>{user_id}</code> id egasi <b>{name}</b> sizga to'lov chekini yubordi.", reply_markup=check_pay)
    await msg.answer(text)
    await state.finish()

@dp.message_handler(state=PayState.firstState)
async def oshibka(msg: types.Message):
    await msg.answer("<b>❗️❗️❗️Iltimos to'lov qilib, to'lov chekini yuboring!!!</b>")

@dp.callback_query_handler(text='yes', state="*")
async def chekni_tekshirish(call: CallbackQuery, state: FSMContext):
    await call.answer("Tasdiqlanmoqda...")
    await bot.send_message(chat_id=982935447, text="Marhamat user id sini yuboring!!!")
    await PayCheck.getState.set()


@dp.message_handler(user_id=982935447, state=PayCheck.getState)
async def book_send(msg: types.Message, state: FSMContext):
    user_id = msg.text

    for k, v in feruza.items():
        if v == user_id:
            await bot.send_message(chat_id=634448116, text=f"<b>Xurmatli Feruza Jumayeva, <code>{k}</code> ushbu fullname ga ega bo'lgan telegram foydalanuvchisi siz bergan link orqali kitobni sotib oldi</b>")

    
    pdf = InputFile(path_or_bytesio="Book/Masala_kitobi_1_qism.pdf")
    await bot.send_document(chat_id=user_id, document=pdf, caption="<b>Xaridingiz uchun tashakkur😊</b>\nBilimingizga bilim qo'shilsin.\n\nMuommo bo'lsa @Asliddinbek_official xizmatga tayyor.")
    await bot.send_message(chat_id=982935447, text=f"✅ {user_id} id egasiga kitob muvaffaqqiyatli yuborildi")
    await state.finish()
    


@dp.callback_query_handler(text='no', state='*')
async def chekni_otkaz(call: CallbackQuery, state: FSMContext):
    await call.answer(text="Rad etildi")
    await bot.send_message(chat_id=982935447, text="Marhamat user id sini yuboring!!!")
    await PayCheck.sendState.set()

@dp.message_handler(user_id=982935447, state=PayCheck.sendState)
async def book_send(msg: types.Message, state: FSMContext):
    user_id = msg.text
    await bot.send_message(chat_id=user_id, text="<b>❌ Siz to'lov qilmagansiz!!!\n\n</b>♻️ Iltimos qaytadan urinib ko'ring!!!")
    await bot.send_message(chat_id=982935447, text=f"❌ {user_id} id egasi cheki tasdiqlanmadi")
    await state.finish()


# --------------------------------------------------------------------------------------------------------------------------------------

@dp.message_handler(Text("👨‍💻Admin bilan aloqa"), state='*')
async def book_show(msg: types.Message):
    await msg.delete()
    await msg.answer("<b>Qo'llab-quvvatlash yoki reklama xizmatlari bo'yicha admin bilan aloqaga chiqing👇👇👇</b>\n\n"
                     "https://t.me/Asliddinbek_official")