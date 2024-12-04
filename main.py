import logging

from aiogram import types, executor
from config import bot, dp
import logging
import os


@dp.message_handler(commands="start")
async def start_handler(message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"Hello! Your Telegram ID is {message.from_user.id}"
    )

@dp.message_handler(commands=["meme"])
async def meme_handler(message: types.Message):
    photo_path = os.path.join('media', 'istockphoto-538665020-612x612.jpg')
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo=photo, caption='Meme')

#  =====================================================
@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.answer(message.text)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
