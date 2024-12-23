
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



cancel_markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
cancel_button = KeyboardButton("Cancel")
cancel_markup.add(cancel_button)

start_markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
start_markup.add(KeyboardButton('/start'), KeyboardButton('/help'),
                 KeyboardButton('/quiz'), KeyboardButton('/registration'),
                 KeyboardButton('/store'),KeyboardButton('/add_product'),
                 KeyboardButton('/delete_product'))

submit = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
submit.add(KeyboardButton("Yes"), KeyboardButton('No'))