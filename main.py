import logging

from aiogram import Bot, Dispatcher, executor, types

from config import API_TOKEN
from sqlite_function import *
from buttons import *
from aiogram.dispatcher.filters import Text

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# baza create
create_db()
create_table_users()
create_table_category()
create_table_books()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    telegram_id = message.from_user.id
    users = select_users(telegram_id)
    if users is None:
        await message.reply("Kontaktni ulashing / Поделитесь контактом🙏", reply_markup=phone_number)
    else:
        await message.reply("Bosh menu!", reply_markup=menu)


@dp.message_handler(content_types='contact')
async def echo(message: types.Message):
    username = message.from_user.username
    telegram_id = message.from_user.id
    phone_number = message.contact['phone_number']

    users = select_users(telegram_id)
    if users is None:
        insert_users(username, telegram_id, phone_number)
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
    data = select_by_id_book(id)
    await call.message.answer(data)
    # await bot.send_photo(chat_id=call.from_user.id, photo=data[4], caption=f"Kitob nomi: {data[2]} \n\n{data[3]}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
