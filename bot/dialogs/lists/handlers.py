from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Select, Button

from .getters import REMINDERS
from bot.states.reminder import ReminderSG


async def selected_reminder(
    callback: CallbackQuery,
    widget: Select,
    dialog_manager: DialogManager,
    item_id: str,
):
    ctx = dialog_manager.current_context()
    ctx.dialog_data.update(reminder_id=item_id)
    await dialog_manager.next()


async def on_set_reminder(
    callback: CallbackQuery,
    widget: Button,
    dialog_manager: DialogManager,
):
    reminder = REMINDERS[0]
    await dialog_manager.start(
        ReminderSG.start,
        data={
            "reminder": {
                "id": reminder.id,
                "description": reminder.description,
                "date": reminder.date,
                "time": reminder.time,
                "period": reminder.period,
                "files": reminder.files,
            }
        },
    )


async def on_done_reminder(
    callback: CallbackQuery,
    widget: Button,
    dialog_manager: DialogManager,
):
    await callback.answer("Выполнено!")
    await dialog_manager.back()


async def on_delete_reminder(
    callback: CallbackQuery,
    widget: Button,
    dialog_manager: DialogManager,
):
    await callback.answer("Удалено!")
    await dialog_manager.back()


async def on_set_passed(
    callback: CallbackQuery,
    widget: Button,
    dialog_manager: DialogManager,
):
    reminder = REMINDERS[0]
    await dialog_manager.start(
        ReminderSG.start,
        data={
            "reminder": {
                "id": reminder.id,
                "description": reminder.description,
                "date": None,
                "time": reminder.time,
                "period": reminder.period,
                "files": reminder.files,
            }
        },
    )
