from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from utils.reply_builder import get_keyboard
from aiogram import F

async def start_cmd(message: Message):
    await message.answer(
        "👋 Привет! Я бот для обучения работе с Mozabook.\n\n"
        "Вот что я умею:\n"
        "/start - Начать работу\n"
        "/help - Помощь\n"
        "/mozabook - Основы работы с Mozabook",reply_markup=get_keyboard("📘 Почати/Продовжити навчання", "📝 Пройти тестування", "📊 Мій прогрес", "❓ Часті питання (FAQ)")
    )

async def cmd_test(message: Message):
    await message.answer(
        "Обери модуль:",
        reply_markup=get_keyboard("Перші кроки в системі Mozaik", "Робота з документами", "Інтерактивне наповнення", sizes = (3, 1))
    )

async def cmd_study(message: Message):
    await message.answer(
        "Обери модуль:",
        reply_markup=get_keyboard("Перші кроки в системі Mozaik", "Робота з документами", "Інтерактивне наповнення", sizes = (3, 1))
        )

async def cmd_progress(message: Message):
    await message.answer()



async def cmd_help(message: Message):
    await message.answer(
        "Обери тему запитання:",
        reply_markup=get_keyboard("Як зареєструвати клас?", "Як створити відеоурок?", "Як оцінити учня?", sizes = (3, 1))
    )



def register_basic_commands(dp: Dispatcher):
    dp.message.register(start_cmd, Command("start"))
    dp.message.register(cmd_study, F.text == "📘 Почати/Продовжити навчання")
    dp.message.register(cmd_test, F.text == "📝 Пройти тестування")
    dp.message.register(cmd_progress, F.text == "📊 Мій прогрес")
    dp.message.register(cmd_help, F.text == "❓ Часті питання (FAQ)")
