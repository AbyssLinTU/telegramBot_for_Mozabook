from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "👋 Привет! Я бот для обучения работе с Mozabook.\n\n"
        "Вот что я умею:\n"
        "/start - Начать работу\n"
        "/help - Помощь\n"
        "/mozabook - Основы работы с Mozabook"
    )


@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "📚 Доступные команды:\n\n"
        "/start - Начать работу\n"
        "/help - Показать это сообщение\n"
        "/mozabook - Основы работы с Mozabook\n\n"
        "Если у вас есть вопросы, используйте команду /mozabook"
    )


@dp.message(Command("mozabook"))
async def cmd_mozabook(message: Message):
    await message.answer(
        "📖 Mozabook - это платформа для образовательных учреждений.\n\n"
        "Основные функции:\n"
        "1. Создание и управление уроками\n"
        "2. Работа с электронным журналом\n"
        "3. Общение с учениками\n"
        "4. Загрузка и хранение материалов\n\n"
        "Для более подробной информации используйте команды:\n"
        "/lessons - Работа с уроками\n"
        "/journal - Работа с журналом\n"
        "/materials - Работа с материалами"
    )


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
