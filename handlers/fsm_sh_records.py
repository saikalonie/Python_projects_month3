
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMShop(StatesGroup):
    model_name = State()
    size = State()
    category = State()
    price = State()
    photo = State()
    submit = State()


async def start_fsm_sh_records(message: types.Message):
    await message.answer('Enter name of the model:')
    await FSMShop.model_name.set()


async def load_model_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['model_name'] = message.text

    await FSMShop.next()
    await message.answer('Enter size: ')


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await FSMShop.next()
    await message.answer('Enter category: ')


async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await FSMShop.next()
    await message.answer('Enter price: ')

async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)

    await FSMShop.next()
    await message.answer('Attach photo of the product: ')

async def load_photo(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await FSMShop.next()
    await message.answer_photo(photo=data['photo'],
                         caption=f'Название модели: {data["model_name"]}\n'
                         f'Размер: {data["size"]}\n'
                         f'Категория: {data["category"]}\n'
                         f'Стоимость: {data["price"]}\n')

async def load_submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'Yes':
        async with state.proxy() as data:
            await message.answer('Product is successfully added to data base !')
        await state.finish()

    elif message.text.lower() == 'No':
        await message.answer('Canceled.')
        await state.finish()

    else:
        await message.answer('Enter Yes or No.')


def register_fsm_sh_records_handlers(dp: Dispatcher):
    dp.register_message_handler(start_fsm_sh_records, commands=['add_product'], state=None)
    dp.register_message_handler(load_model_name, state=FSMShop.model_name)
    dp.register_message_handler(load_size, state=FSMShop.size)
    dp.register_message_handler(load_category, state=FSMShop.category)
    dp.register_message_handler(load_price, state=FSMShop.price)
    dp.register_message_handler(load_photo, state=FSMShop.photo, content_types=['photo'])
    dp.register_message_handler(load_submit, state=FSMShop.submit)
