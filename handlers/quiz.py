
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot

async def quiz_1(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)

    button = InlineKeyboardButton("Далее", callback_data='quiz_2')

    # button2 = InlineKeyboardButton("Далее", callback_data='quiz_3')

    keyboard.add(button)
    # keyboard.add(button2)



    question = 'TOEFL,  IELTS or Duolingo?'
    answer = ['TOEFL', 'IELTS', 'Duolingo']


    await bot.send_poll(
        chat_id=message.from_user.id,   # куда отправить
        question=question,      #  вопрос
        options=answer,          # Ответы
        is_anonymous=False,     # Анонимный или нет
        type='quiz',            # тип опросника
        correct_option_id=0,    # id правильного ответа
        explanation='do not hesitate, please!',  # тест при неправильном ответе
        open_period=60,         # Время работы опросника
        reply_markup=keyboard  # Добавление кнопки
    )



async def quiz_2(call: types.CallbackQuery):
    # keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    # button2 = InlineKeyboardButton("Следущее", callback_data='quiz_3')
    # keyboard.add(button2)


    question = 'Python, JavaScript, Java, PHP and Swift'
    answer = ['Python', 'JavaScript', 'Java', 'PHP', 'Swift']

    await bot.send_poll(
        chat_id=call.from_user.id,   # куда отправить
        question=question,      # сам вопрос
        options=answer,          # Ответы
        is_anonymous=True,     # Анонимный или нет
        type='quiz',            # тип опросника
        correct_option_id=0,    # id правильного ответа
        explanation='Всё с тобой понятно -_- ',  # тест при неправильном ответе
        open_period=180
    )

async def quiz_3(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = InlineKeyboardButton("следующее", callback_data='quiz_3')
    keyboard.add(button)

    image_path = 'media/images(2).jpg'

    await bot.send_photo(
        chat_id=call.from_user.id,
        photo=open(image_path, 'rb'))

    question = 'What does this picture represent?'
    options = ['Nature', 'City', 'Ocean', 'Mountains']

    await bot.send_poll(
        chat_id= call.from_user.id,
        question=question,
        options=options,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        reply_markup=keyboard
    )

def register_quiz_handlers(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands='quiz')
    dp.register_callback_query_handler(quiz_2, text='quiz_2')
    dp.register_callback_query_handler(quiz_2, text='quiz_3')

