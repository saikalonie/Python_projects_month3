import logging

from aiogram import executor

from config import bot, dp, Admins
import logging
from handlers import commands, echo, quiz, fsm_reg, fsm_store, send_products, delete_product, edit_product
from db import main_db
import buttons


async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='Бот включен!')
        await bot.send_message(chat_id=admin, text='Бот включен!',
                               reply_markup=buttons.start_markup)
        await main_db.DataBase_create()


commands.register_commands(dp)
quiz.register_quiz_handlers(dp)

fsm_reg.register_fsmreg_handlers(dp)
fsm_store.store_fsm_handlers(dp)

send_products.register_handlers(dp)
delete_product.register_handlers(dp)
edit_product.register_handlers(dp)

echo.register_echo_handler(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
