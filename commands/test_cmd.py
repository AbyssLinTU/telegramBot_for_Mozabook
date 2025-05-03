from aiogram import Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import State, StatesGroup
from utils.reply_builder import get_keyboard
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F


class TestStates(StatesGroup):
    waiting_for_answer = State()  # Ожидаем ответ на вопрос
    test_completed = State()      # Тест завершен


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


async def show_question(message: Message, state: FSMContext):
    data = await state.get_data()
    question = questions[data["current_question"]]

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=opt, callback_data=f"answer_{opt}")]
        for opt in question["options"]
    ])

    await message.answer(
        f"Вопрос {data['current_question'] + 1}/{data['total_questions']}:\n"
        f"{question['text']}",
        reply_markup=keyboard
    )


@dp.message(Command("start_test"))
async def start_test(message: Message, state: FSMContext):
    await state.update_data(
        current_question=0,
        correct_answers=0,
        total_questions=len(questions)
    )
    await show_question(message, state)
    await state.set_state(TestStates.waiting_for_answer)
