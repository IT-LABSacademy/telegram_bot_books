from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


phone_number = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton("📞 Telefon raqamni yuborish!", request_contact=True)  
        ]
    ],
    resize_keyboard=True
)


menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton("Bosh menu")  
        ]
    ],
    resize_keyboard=True
)
