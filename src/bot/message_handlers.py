from aiogram.filters import Command
from aiogram import types, Router

message_router = Router()

@message_router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Hello wassup again")