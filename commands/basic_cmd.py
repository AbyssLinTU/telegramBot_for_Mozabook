from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command


async def start_cmd(message: Message):
    await message.answer(
        "👋 Привет! Я бот для обучения работе с Mozabook.\n\n"
        "Вот что я умею:\n"
        "/start - Начать работу\n"
        "/help - Помощь\n"
        "/mozabook - Основы работы с Mozabook"
    )


async def cmd_help(message: Message):
    await message.answer(
        "📚 Доступные команды:\n\n"
        "/start - Начать работу\n"
        "/help - Показать это сообщение\n"
        "/mozabook - Основы работы с Mozabook\n\n"
        "Если у вас есть вопросы, используйте команду /mozabook"
    )


def register_basic_commands(dp: Dispatcher):
    dp.message.register(start_cmd, Command("start"))
    dp.message.register(cmd_help, Command("help"))
