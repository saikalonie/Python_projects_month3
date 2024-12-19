#fsm_store.py
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import buttons
from aiogram.dispatcher import FSMContext
from db import main_db

class store_fsm(StatesGroup):
    name_product = State()
    size = State()
    category = State()
    price = State()
    product_id = State()
    info_product = State()
    photo = State()
    collection = State()
    submit = State()

async def start_fsm_store(message: types.Message):
    await message.answer('Enter the name of the product: ',
                         reply_markup=buttons.cancel_markup)
    await store_fsm.name_product.set()


async def load_name_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_product'] = message.text

    await store_fsm.next()
    await message.answer('Enter the size of the product: ')


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await store_fsm.next()
    await message.answer('Enter the category of the product: ')

async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await store_fsm.next()
    await message.answer('Enter the price of the product: ')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await store_fsm.next()
    await message.answer('Eneter the ID of the product: ')


async def load_product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await store_fsm.next()
    await message.answer('Enter the information about the product: ')


async def load_info_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['info_product'] = message.text

    await store_fsm.next()
    await message.answer('Attach a photo of the product: ')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

        await store_fsm.next()
        await message.answer('Enter the collection name: ')

async def load_collection(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
            data['collection'] = message.text

    await store_fsm.next()

    await message.answer(f'Is the data correct?', reply_markup=buttons.submit)
    await message.answer_photo(photo=data['photo'],
                               caption=f'Name - {data["name_product"]}\n'
                                       f'Size - {data["size"]}\n'
                                       f'Category - {data["category"]}\n'
                                       f'Product ID - {data["product_id"]}\n'
                                       f'Information of the product - {data["info_product"]}\n'
                                       f'Collection - {data["collection"]}\n'
                                       f'Price- {data["price"]}\n')

async def load_submit(message: types.Message, state: FSMContext):
    if message.text == 'Yes':
        async with state.proxy() as data:
            await main_db.sql_insert_store(
                name_product=data['name_product'],
                size=data['size'],
                price=data['price'],
                product_id=data['product_id'],
                photo=data['photo']
            )
            await main_db.sql_insert_store_detail(
                category=data['category'],
                info_product=data['info_product'],
                product_id=data['product_id']
            )
            await main_db.sql_insert_collection_product(
                product_id=data['product_id'],
                collection=data['collection']
            )
            await message.answer('Your data in database!')
            await state.finish()

    elif message.text == 'No':
        await message.answer('Ok, data is deleted!')
        await state.finish()

    else:
        await message.answer('Enter Yes or No!')


def store_fsm_handlers(dp: Dispatcher):
    dp.register_message_handler(start_fsm_store, commands=['add_product'])
    dp.register_message_handler(load_name_product, state=store_fsm.name_product)
    dp.register_message_handler(load_size, state=store_fsm.size)
    dp.register_message_handler(load_category, state=store_fsm.category)
    dp.register_message_handler(load_price, state=store_fsm.price)
    dp.register_message_handler(load_product_id, state=store_fsm.product_id)
    dp.register_message_handler(load_info_product, state=store_fsm.info_product)
    dp.register_message_handler(load_collection, state=store_fsm.collection)
    dp.register_message_handler(load_photo, state=store_fsm.photo, content_types=['photo'])
    dp.register_message_handler(load_submit, state=store_fsm.submit)






