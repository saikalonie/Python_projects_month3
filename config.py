
from aiogram import Bot, Dispatcher
from decouple import config
Admins = [795236182, ]

token = config("TOKEN")
bot = Bot(token=token)
dp = Dispatcher(bot)
