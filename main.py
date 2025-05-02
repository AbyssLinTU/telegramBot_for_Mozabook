from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from config import BOT_TOKEN
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import utils.keyboards as kb
from commands.basic_cmd import register_basic_commands
from utils.reply_builder import get_keyboard
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


register_basic_commands(dp)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())