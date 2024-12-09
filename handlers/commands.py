from aiogram import types, Dispatcher
from config import bot
import os

# @dp.message_handler(commands="start")
async def start_handler(message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"Hello! Your Telegram ID is {message.from_user.id}"
    )

# @dp.message_handler(commands=["meme"])
async def meme_handler(message: types.Message):
    photo_path = os.path.join('media', 'istockphoto-538665020-612x612.jpg')
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo=photo, caption='Meme')

# async def dice_handler(massage: types.Message):
#   user_dice =


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(meme_handler, commands=['meme'])
