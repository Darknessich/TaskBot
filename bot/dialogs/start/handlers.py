from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.states.new_reminder import NewReminderSG


async def go_new_reminder(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.start(state=NewReminderSG.start)


async def go_reminders_list():
    pass


async def go_passed_list():
    pass


async def go_setup_language():
    pass
