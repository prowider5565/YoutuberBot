from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.types import FSInputFile
from aiogram.filters import Command
from aiogram import types, Router
import os

from src.settings import settings
from .config import bot


message_router = Router()


@message_router.message(Command('webapp'))
async def send_welcome(message: types.Message):
    web_app_button = InlineKeyboardButton(
        text="Open WebApp", 
        web_app=WebAppInfo(url=settings.DOMAIN)     
    )   
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[web_app_button]])
    
    await message.answer("Click the button below to open the web app:", reply_markup=keyboard)
