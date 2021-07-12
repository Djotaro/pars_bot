from aiogram.types import ReplyKeyboardRemove,KeyboardButton,InlineKeyboardButton,ReplyKeyboardMarkup




button1 = KeyboardButton('Хакатоны')
button2 = KeyboardButton('Гранты')


markup3 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1).add(button2)








