from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot

async def quiz_1(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = InlineKeyboardButton("Далее", callback_data='quiz_2')
    keyboard.add(button)

    question = 'TOEFL, IELTS or Duolingo?'
    answer = ['TOEFL', 'IELTS', 'Duolingo']

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='Do not hesitate, please!',
        open_period=60,
        reply_markup=keyboard
    )


async def quiz_2(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = InlineKeyboardButton("Следующее", callback_data='quiz_3')
    keyboard.add(button)

    question = 'Which language is the best?'
    answer = ['Python', 'JavaScript', 'Java', 'PHP', 'Swift']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='Obviously, Python is the best!',
        open_period=60,
        reply_markup=keyboard
    )


async def quiz_3(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = InlineKeyboardButton("Закончить", callback_data='quiz_end')
    keyboard.add(button)

    image_path = 'media/images (2).jpg'

    with open(image_path, 'rb') as photo:
        await bot.send_photo(chat_id=call.from_user.id, photo=photo)

    question = 'What does this picture represent?'
    options = ['Nature', 'City', 'Ocean', 'Mountains']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=options,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='Look closely at the picture!',
        reply_markup=keyboard
    )


def register_quiz_handlers(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands='quiz')
    dp.register_callback_query_handler(quiz_2, text='quiz_2')
    dp.register_callback_query_handler(quiz_3, text='quiz_3')
