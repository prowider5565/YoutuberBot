from aiogram import types, Bot, Dispatcher
import logging

from src.bot.message_handlers import message_router
from src.settings import settings


logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()
routers = [message_router]
dp.include_routers(*routers)

