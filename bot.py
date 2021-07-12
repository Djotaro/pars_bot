from aiogram import Bot, Dispatcher, executor,types
from aiogram.dispatcher.filters import Command,Text
from config import TOKEN, CHAT_CONTESTS
import keyboards as kb

import requests


from time import sleep
from datetime import datetime

bot = Bot(TOKEN)
dp = Dispatcher(bot)
chat_id = CHAT_CONTESTS

@dp.message_handler(commands= 'start')
async def echo_message(message: types.Message):
    await message.reply("Доступные каналы", reply_markup=kb.markup3)


@dp.message_handler(Text(equals='Гранты'))
async def grants_message(message: types.Message):
         await message.answer("Aхмат сила")


@dp.message_handler(Text(equals='Хакатоны'))
async def grants_message(message: types.Message):
         await message.answer("Чечня круто")


async def send_message_channel(dp):
    while True:
        req = requests.get('https://parsing-web-app.herokuapp.com/api/get/contests').json()
        for unknown_link in req['links']:
            await bot.send_message(chat_id, text=unknown_link)
            sleep(15)
        print(f'Увидимся через неделю - {datetime.now()}')
        sleep(604800)
        print(f'Я вернулся - {datetime.now()}')


if __name__ == '__main__':
    executor.start_polling(dp,on_startup=send_message_channel)
