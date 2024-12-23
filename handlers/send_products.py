from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from db import main_db

user_product_index = {}


async def start_send_products(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    button_all_products = types.InlineKeyboardButton('Вывести все товары', callback_data='send_all_products')
    button_one_product = types.InlineKeyboardButton('Вывести по одному', callback_data='send_one_products')

    keyboard.add(button_all_products, button_one_product)

    await message.answer('Выберите как просмотреть товары: ', reply_markup=keyboard)


async def send_all_products(call: types.CallbackQuery):
    products = main_db.fetch_all_products()

    if products:
        for product in products:
            caption = (
                f'Name - {product["name_product"]}\n'
                f'Size - {product["size"]}\n'
                f'Category - {product["category"]}\n'
                f'Product ID - {product["product_id"]}\n'
                f'Description - {product["info_product"]}\n'
                f'Price - {product["price"]}\n'
            )
            await call.message.answer_photo(photo=product['photo'], caption=caption)
    else:
        await call.message.answer('Data is empty! No more products.')


async def send_one_product(call: types.CallbackQuery):
    user_id = call.from_user.id
    products = main_db.fetch_all_products()

    if not products:
        await call.message.answer('Data is empty! No more products.')
        return

    if user_id not in user_product_index:
        user_product_index[user_id] = 0

    current_index = user_product_index[user_id]

    if current_index >= len(products):
        await call.message.answer('No more products to show.')
        return

    product = products[current_index]

    caption = (
        f'Name - {product["name_product"]}\n'
        f'Size - {product["size"]}\n'
        f'Category - {product["category"]}\n'
        f'Product ID - {product["product_id"]}\n'
        f'Description - {product["info_product"]}\n'
        f'Price - {product["price"]}\n'
    )

    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    button_next = types.InlineKeyboardButton('Далее', callback_data='next_product')
    keyboard.add(button_next)

    await call.message.answer_photo(photo=product['photo'], caption=caption, reply_markup=keyboard)

    user_product_index[user_id] += 1


async def next_product(call: types.CallbackQuery):
    await send_one_product(call)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_send_products, commands=['store'])
    dp.register_callback_query_handler(send_all_products, Text(equals='send_all_products'))
    dp.register_callback_query_handler(send_one_product, Text(equals='send_one_products'))
    dp.register_callback_query_handler(next_product, Text(equals='next_product'))
