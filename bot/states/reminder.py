from aiogram.fsm.state import State, StatesGroup


class ReminderSG(StatesGroup):
    start = State()
    set_description = State()
    set_date = State()
    set_time = State()
    set_period = State()
    set_files = State()
