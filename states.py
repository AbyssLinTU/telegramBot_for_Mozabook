from aiogram.fsm.state import State, StatesGroup


class TestStates(StatesGroup):
    correct_answer = State()
    wrong_answer = State()
