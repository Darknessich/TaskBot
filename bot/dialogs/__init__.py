from aiogram import Dispatcher
import aiogram_dialog

from . import start, reminder


def setup_dialogs(dp: Dispatcher):
    dp.include_routers(
        *start.get_dialogs(),
        *reminder.get_dialogs(),
    )
    aiogram_dialog.setup_dialogs(dp)
