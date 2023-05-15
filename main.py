import logging

from aiogram import Bot, Dispatcher, executor, types

from config import API_TOKEN
from sqlite_function import *
from buttons import *



# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# baza create
create_db()
create_table_users()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    telegram_id = message.from_user.id
    users = select_users(telegram_id)
    if users is None:
        await message.reply("Kontaktni ulashing / Поделитесь контактом🙏", reply_markup=phone_number)
    else:
        await message.reply("Salom!")


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
        await message.reply("Bosh menu")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
