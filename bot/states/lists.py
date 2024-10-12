from aiogram.fsm.state import State, StatesGroup


class RemindersListSG(StatesGroup):
    list = State()
    reminder = State()

class PassedListSG(StatesGroup):
    list = State()
    reminder = State()