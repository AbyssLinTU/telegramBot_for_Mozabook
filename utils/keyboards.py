from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📖 Mozabook"),
            KeyboardButton(text="❓ Допомога")
        ]
    ],
    resize_keyboard=True
)
