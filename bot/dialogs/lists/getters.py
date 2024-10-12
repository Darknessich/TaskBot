from typing import TYPE_CHECKING


from aiogram.types import Document
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner
from sqlalchemy.ext.asyncio import AsyncSession

from services.repository import ReminderRepository
from models.reminders import Status

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner


def get_time_str(time: int) -> str:
    return f"{time // 60 :02}:{time % 60 :02}"


def get_period_str(period: int, default: str) -> str:
    return (
        default
        if not period
        else f"{period // 1440}d. {(period // 60) % 24}h. {period % 60}m."
    )


def get_files_str(files: list[Document]) -> str:
    return "\n".join([f"- {file.file_name}" for file in files])


async def get_reminder_list_window(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    session: AsyncSession,
    **kwargs,
):
    reminders = await ReminderRepository.get_reminders_by_status(
        session=session,
        chat_id=dialog_manager.event.message.chat.id,
        status=Status.ACTIVE,
    )

    return {
        "amount_reminders": i18n.amount.reminders(),
        "amount": len(reminders),
        "button_main_menu": i18n.button.main.menu(),
        "reminders": reminders,
    }


async def get_reminder_window(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    session: AsyncSession,
    **kwargs,
):
    ctx = dialog_manager.current_context()
    ctx.dialog_data.update(session=session)
    reminder_id: int = ctx.dialog_data.get("reminder_id")
    reminder = await ReminderRepository.get_reminder_by_id(session, reminder_id)

    date = reminder.datetime.date()
    time = reminder.datetime.hour * 60 + reminder.datetime.minute
    period = (
        reminder.period.days * 1440 + reminder.period.seconds // 60
        if reminder.period
        else 0
    )
    return {
        "header_description": i18n.header.description(),
        "reminder_description": reminder.description,
        "header_date": i18n.header.date(),
        "reminder_date": date,
        "header_time": i18n.header.time(),
        "reminder_time": get_time_str(time),
        "header_period": i18n.header.period(),
        "reminder_period": get_period_str(period, i18n.not_.periodically()),
        "header_files": i18n.header.files(),
        "reminder_files": get_files_str(reminder.files),
        "button_set_reminder": i18n.button.set.reminder(),
        "button_done": i18n.button.done(),
        "button_delete": i18n.button.delete(),
        "button_back": i18n.button.back(),
        "button_set_passed": i18n.button.set.passed(),
    }


async def get_passed_list_window(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    session: AsyncSession,
    **kwargs,
):
    reminders = await ReminderRepository.get_reminders_by_status(
        session=session,
        chat_id=dialog_manager.event.message.chat.id,
        status=Status.DONE,
    )

    return {
        "amount_passed": i18n.amount.passed(),
        "amount": len(reminders),
        "button_main_menu": i18n.button.main.menu(),
        "reminders": reminders,
    }
