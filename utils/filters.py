from aiogram.filters import Filter
from aiogram.types import Message, Bot
from config import ADMIN_IDS


class IsAdmin(Filter):
    def __init__(self) -> None:
        pass

    async def __call__(self, message: Message, bot: Bot) -> bool:
        return message.from_user.id in ADMIN_IDS
