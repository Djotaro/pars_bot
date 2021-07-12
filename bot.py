from aiogram import Bot, Dispatcher, executor,types
from aiogram.dispatcher.filters import Command,Text
from config import TOKEN, CHAT_CONTESTS
import keyboards as kb

import requests


bot = Bot(TOKEN)
dp = Dispatcher(bot)
chat_id = CHAT_CONTESTS

@dp.message_handler(commands= 'start')
async def echo_message(message: types.Message):
    await message.reply("Доступные каналы \n ", reply_markup=kb.inline_kb1)


@dp.message_handler(Text(equals='Гранты'))
async def grants_message(message: types.Message):
         await message.answer("Aхмат сила")


@dp.message_handler(Text(equals='Хакатоны'))
async def grants_message(message: types.Message):
         await message.answer("Чечня круто")


async def send_message_channel(message:types.Message):
    req = requests.get('https://parsing-web-app.herokuapp.com/api/get/contests').json()
    for unknown_link in req['links']:
        await message.answer(unknown_link)


if __name__ == '__main__':
    executor.start_polling(dp,on_startup=send_message_channel)
