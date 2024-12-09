# commands.py
from aiogram import types, Dispatcher
from pyexpat.errors import messages

from config import bot
import os
import random
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


games = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']

async def dice_handler(message: types.Message):
    if 'game' in message.text.lower():
        game = random.choice(games)
        await message.answer_dice(emoji=game)

def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(meme_handler, commands=['meme'])
    dp.register_message_handler(dice_handler, commands=['dice', 'game'])

