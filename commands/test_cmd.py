from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from utils.reply_builder import get_keyboard
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F, Dispatcher


class TestStates(StatesGroup):
    in_quiz = State()  # Ожидаем ответ на вопрос


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


async def start_quiz_handler(message: Message, state: FSMContext, questions: list):
    await state.update_data(
        count_correct=0,
        count_quiz=0,
        questions=questions,
        current_quiz=0
    )
    await ask_quiz(message, state)


async def ask_quiz(message: Message, state: FSMContext):
    data = await state.get_data()
    current_quiz = data['current_quiz']
    questions = data['questions']
    if current_quiz >= len(questions):
        await message.answer(
            f"Тест завершен!\n"
            f"Правильных ответов: {data['count_correct']}/{data['count_quiz']}\n"
            f"Успешность: {data['count_correct'] / data['count_quiz'] * 100:.0f}%"
        )
        await state.clear()
        return
    quiz_data = questions[current_quiz]

    await message.answer(f"Вопрос {current_quiz+1}: \n {quiz_data['text']}", reply_markup=get_keyboard(*quiz_data['options']))
    await state.set_state(TestStates.in_quiz)


async def handle_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    current_quiz = data['current_quiz']
    questions = data['questions']
    quiz_data = questions[current_quiz]
    if message.text == quiz_data['correct']:
        data["count_correct"] += 1
        await message.answer("✅ Верно!")
    else:
        await message.answer(f"❌ Неверно! Правильный ответ: {quiz_data['correct']} \n Пояснення: {quiz_data['explanation']}")
    data["count_quiz"] += 1
    data["current_quiz"] += 1
    await state.update_data(**data)
    await ask_quiz(message, state)


async def quiz_wrapper(message: Message, state: FSMContext):
    await start_quiz_handler(message, state, questions)


def register_test(dp: Dispatcher, trigger, questions: list):
    """
    Функция для создание тестов

    Аргументи:
        dp (Dispatcher): Диспачер с аиограма
        trigger : Тригер по которому будет визываться тест. (Пример Command(test), F.text='тест')
        questions: Список всех вопросов с ответами
        Пример структури questions:
            questions = [
                {
                    "text": "Земля плоская?",
                    "options": ["Да", "Нет"],
                    "correct": "Нет",
                    "explanation": "Земля имеет форму геоида"
                },
                {
                    "text": "Python - интерпретируемый язык?",
                    "options": ["Да", "Нет"],
                    "correct": "Да",
                    "explanation": "Python выполняется через интерпретатор"
                }
            ]
    """
    dp.message.register(
        quiz_wrapper,
        trigger
    )
    dp.message.register(handle_answer,  TestStates.in_quiz, F.text)
