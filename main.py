from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from config import BOT_TOKEN
from commands.basic_cmd import register_basic_commands
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from utils.reply_builder import get_keyboard

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# register_test_cmd(dp)
register_basic_commands(dp)

<< << << < HEAD
== == == =


class TestStates(StatesGroup):
    question_1 = State()
    question_2 = State()
    finished = State()


@dp.message(Command("smart_test"))
async def start_smart_test(message: Message, state: FSMContext):
    # Инициализируем счетчики
    await state.update_data(
        count_correct=0,
        count_quiz=0
    )
    await message.answer(
        "Вопрос 1: 2+2=?",
        reply_markup=get_keyboard('4', '6')
    )
    await state.set_state(TestStates.question_1)

# 4. Обработчик первого вопроса


@dp.message(TestStates.question_1, F.text)
async def handle_question_1(message: Message, state: FSMContext):
    data = await state.get_data()

    if message.text == '4':
        data["count_correct"] += 1
        await message.answer("✅ Верно!")
    else:
        await message.answer("❌ Неверно! Правильный ответ: 4")

    data["count_quiz"] += 1
    await state.update_data(**data)

    await message.answer(
        "Вопрос 2: Столица Франции?",
        reply_markup=get_keyboard('ПАриж', 'РИга')
    )
    await state.set_state(TestStates.question_2)

# 5. Обработчик второго вопроса


@dp.message(TestStates.question_2, F.text)
async def handle_question_2(message: Message, state: FSMContext):
    data = await state.get_data()

    if message.text.lower() == 'париж':
        data["count_correct"] += 1
        await message.answer("✅ Верно!")
    else:
        await message.answer("❌ Неверно! Правильный ответ: Париж")

    data["count_quiz"] += 1
    await state.update_data(**data)

    # Выводим результаты
    await message.answer(
        f"Тест завершен!\n"
        f"Правильных ответов: {data['count_correct']}/{data['count_quiz']}\n"
        f"Успешность: {data['count_correct']/data['count_quiz']*100:.0f}%",
    )
    await state.set_state(TestStates.finished)
    await state.clear()


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


>>>>>> > Georgy


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
