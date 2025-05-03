from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from config import BOT_TOKEN
from commands.basic_cmd import register_basic_commands
from commands.test_cmd import register_test

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
questions = [
    {
        "id": 1,
        "text": "Земля плоская?",
        "options": ["Да", "Нет"],
        "correct": "Нет",
        "explanation": "Земля имеет форму геоида"
    },
    {
        "id": 2,
        "text": "Python - интерпретируемый язык?",
        "options": ["Да", "Нет"],
        "correct": "Да",
        "explanation": "Python выполняется через интерпретатор"
    }
]

# register_test_cmd(dp)
register_basic_commands(dp)
register_test(dp, F.text == "Перші кроки в системі Mozaik", questions)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
