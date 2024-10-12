from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Select, Button

from bot.states.reminder import ReminderSG
from services.repository import ReminderRepository
from models.reminders import Status


async def selected_reminder(
    callback: CallbackQuery,
    widget: Select,
    dialog_manager: DialogManager,
    item_id: str,
):
    ctx = dialog_manager.current_context()
    ctx.dialog_data.update(reminder_id=int(item_id))
    await dialog_manager.next()


async def on_set_reminder(
    callback: CallbackQuery,
    widget: Button,
    dialog_manager: DialogManager,
):
    ctx = dialog_manager.current_context()
    session = ctx.dialog_data.get("session")
    reminder_id = ctx.dialog_data.get("reminder_id")

    reminder = await ReminderRepository.get_reminder_by_id(session, reminder_id)
    time = reminder.datetime.hour * 60 + reminder.datetime.minute
    period = (
        reminder.period.days * 1440 + reminder.period.seconds // 60
        if reminder.period
        else 0
    )
    await dialog_manager.start(
        ReminderSG.start,
        data={
            "reminder": {
                "id": reminder.id,
                "description": reminder.description,
                "date": reminder.datetime.date(),
                "time": time,
                "period": period,
                "files": reminder.files,
            }
        },
    )


async def on_done_reminder(
    callback: CallbackQuery,
    widget: Button,
    dialog_manager: DialogManager,
):
    ctx = dialog_manager.current_context()
    session = ctx.dialog_data.get("session")
    reminder_id = ctx.dialog_data.get("reminder_id")

    await ReminderRepository.update_reminder_status(session, reminder_id, Status.DONE)
    await callback.answer("Выполнено!")
    await dialog_manager.back()


async def on_delete_reminder(
    callback: CallbackQuery,
    widget: Button,
    dialog_manager: DialogManager,
):
    ctx = dialog_manager.current_context()
    session = ctx.dialog_data.get("session")
    reminder_id = ctx.dialog_data.get("reminder_id")

    await ReminderRepository.update_reminder_status(session, reminder_id, Status.DELETE)
    await callback.answer("Удалено!")
    await dialog_manager.back()


async def on_set_passed(
    callback: CallbackQuery,
    widget: Button,
    dialog_manager: DialogManager,
):
    ctx = dialog_manager.current_context()
    session = ctx.dialog_data.get("session")
    reminder_id = ctx.dialog_data.get("reminder_id")

    reminder = await ReminderRepository.get_reminder_by_id(session, reminder_id)
    time = reminder.datetime.hour * 60 + reminder.datetime.minute
    period = (
        reminder.period.days * 1440 + reminder.period.seconds // 60
        if reminder.period
        else 0
    )
    await dialog_manager.start(
        ReminderSG.start,
        data={
            "reminder": {
                "description": reminder.description,
                "date": None,
                "time": time,
                "period": period,
                "files": reminder.files,
            }
        },
    )
