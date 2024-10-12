from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.states.reminder import ReminderSG
from bot.states.lists import RemindersListSG, PassedListSG


async def go_new_reminder(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.start(state=ReminderSG.start)


async def go_reminders_list(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.start(state=RemindersListSG.list)


async def go_passed_list(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.start(state=PassedListSG.list)


async def go_setup_language(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    pass
