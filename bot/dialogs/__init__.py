from aiogram import Dispatcher
import aiogram_dialog

from . import start


def setup_dialogs(dp: Dispatcher):
    dp.include_routers(
        *start.get_dialogs(),
    )
    aiogram_dialog.setup_dialogs(dp)
