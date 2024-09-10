from aiogram import types, Bot, Dispatcher
import logging

from src.settings import settings


logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()


    