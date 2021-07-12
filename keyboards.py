from aiogram.types import ReplyKeyboardRemove,KeyboardButton,InlineKeyboardButton,ReplyKeyboardMarkup,InlineKeyboardMarkup




btn1 = InlineKeyboardButton('Конкурсы!', callback_data='button1',url="https://t.me/TkContests")
# btn2 = InlineKeyboardButton('Конкурсы!', callback_data='button1',url="https://t.me/TkContests")#<---НЕ ТРОГАТЬ
inline_kb1 = InlineKeyboardMarkup().add(btn1)







