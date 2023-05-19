import logging

from aiogram import Bot, Dispatcher, executor, types

from config import API_TOKEN
# from sqlite_function import *
from sqlite_class import Database
from buttons import *
from aiogram.dispatcher.filters import Text

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
db = Database()

# baza create
db.create_table_users()
db.create_table_category()
db.create_table_books()

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    telegram_id = message.from_user.id
    users = db.select_users(telegram_id)
    if users is None:
        await message.reply("Kontaktni ulashing / Поделитесь контактом🙏", reply_markup=phone_number)
    else:
        await message.reply("Bosh menu!", reply_markup=menu)


@dp.message_handler(content_types='contact')
async def echo(message: types.Message):
    username = message.from_user.username
    telegram_id = message.from_user.id
    phone_number = message.contact['phone_number']

    users = db.select_users(telegram_id)
    if users is None:
        db.insert_users(username, telegram_id, phone_number)
        await message.reply("Siz ro'yxatdan o'tdingiz!")
        await message.reply("Bosh menu", reply_markup=menu)
    else:
        await message.reply("Bosh menu", reply_markup=menu)


@dp.message_handler(content_types='photo')
async def echo(message: types.Message):
    print(
        message.photo[-1]['file_id']
    )


@dp.message_handler(text='Bosh menu')
async def echo(message: types.Message):
    markup = select_category_button()
    await message.answer("Bo'limlardan birini tanlang...", reply_markup=markup)


@dp.callback_query_handler(Text(startswith='category_'))
async def grtghrthtr(call: types.CallbackQuery):
    inx = call.data.index("_")
    category_id = call.data[inx+1:]
    markup = select_books_by_category_id_button(category_id)
    await call.message.answer("Kitoblardan birini tanlang...", reply_markup=markup)


@dp.callback_query_handler(Text(startswith='books_'))
async def grtghrthtr(call: types.CallbackQuery):
    inx = call.data.index("_")
    id = call.data[inx+1:]
    data = db.select_by_id_book(id)
    button = types.InlineKeyboardMarkup(row_width=2)
    button.insert(types.InlineKeyboardButton(text="Ortga", callback_data=f"ortga_{data[1]}"))
    await bot.send_photo(chat_id=call.from_user.id, photo=data[4], caption=f"Kitob nomi: {data[2]} \n\n{data[3]}",reply_markup=button)



@dp.callback_query_handler(Text(startswith='ortga_'))
async def grtghrthtr(call: types.CallbackQuery):
    inx = call.data.index("_")
    category_id = call.data[inx+1:]
    markup = select_books_by_category_id_button(category_id)
    await call.message.answer("Kitoblardan birini tanlang...", reply_markup=markup)



@dp.callback_query_handler(text='menu_ortga')
async def grtghrthtr(call: types.CallbackQuery):
    markup = select_category_button()
    await call.message.answer("Bo'limlardan birini tanlang...", reply_markup=markup)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
