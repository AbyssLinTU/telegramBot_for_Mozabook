from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from config import BOT_TOKEN
from commands.basic_cmd import register_basic_commands

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

register_basic_commands(dp)


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
