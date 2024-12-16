from logging import currentframe

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from buttons import cancel_markup, start_markup
from aiogram.types import ReplyKeyboardRemove


class FSMReg(StatesGroup):
    fullname = State()
    Age = State()
    Gender = State()
    Email = State()
    Photo = State()
    Submit = State()


async def start_fsm_reg(message: types.Message):
    await message.answer('Enter your full name:')
    await FSMReg.fullname.set()

async def load_fullname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fullname'] = message.text

    await FSMReg.next()
    await message.answer('Enter your age: ')


async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text

    await FSMReg.next()
    await message.answer('Enter your gender: ')


async def load_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text

    await FSMReg.next()
    await message.answer('Enter your email: ')


async def load_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text

    await FSMReg.next()
    await message.answer('Attach your photo: ')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await FSMReg.next()
    await message.answer(f'Is the data proper?')
    await message.answer_photo(photo=data['photo'],
                               caption=f'ФИО - {data["fullname"]}\n'
                             f'Age - {data["age"]}\n'
                             f'Gender - {data["gender"]}\n'
                             f'Email - {data["email"]}\n')


async def load_submit(message: types.Message, state: FSMContext):
    if message.text == 'Yes':
        async with state.proxy() as data:
            await message.answer('Your data in database!')
            await state.finish()

    elif message.text == 'No':
        await message.answer('Ok, data is deleted!')
        await state.finish()

    else:
        await message.answer('Enter yeas or no!')

async def cancel_fsm(message:types.Message, state:FSMContext):
    current_state = await state.get_state()
    kb = ReplyKeyboardRemove()

    if current_state is not None:
        await state.finish()
        await message.answer('Canceled', reply_markup=kb)

def register_fsmreg_handlers(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='отмена',
                                                 ignore_case=True), state='*')

    dp.register_message_handler(start_fsm_reg, commands=['registration'])
    dp.register_message_handler(load_fullname, state=FSMReg.fullname)
    dp.register_message_handler(load_age, state=FSMReg.Age)
    dp.register_message_handler(load_gender, state=FSMReg.Gender)
    dp.register_message_handler(load_email, state=FSMReg.Email)
    dp.register_message_handler(load_photo, state=FSMReg.Photo, content_types=['photo'])
    dp.register_message_handler(load_submit, state=FSMReg.Submit)
