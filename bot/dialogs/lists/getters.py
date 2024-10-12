from typing import TYPE_CHECKING


from aiogram.types import Document
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from datetime import date, datetime

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner


################


class Reminder:
    id: int = 0
    description: str = "Фиктивное напоминание"
    date = datetime.now().date()
    time: int = 0
    period: int = 0
    files: list[Document] = []


REMINDERS: list[Reminder] = [Reminder()]

###########


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
    **kwargs,
):
    return {
        "amount_reminders": i18n.amount.reminders(),
        "amount": len(REMINDERS),
        "button_main_menu": i18n.button.main.menu(),
        "reminders": REMINDERS,
    }


async def get_reminder_window(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    **kwargs,
):
    reminder: Reminder = REMINDERS[0]
    return {
        "header_description": i18n.header.description(),
        "reminder_description": reminder.description,
        "header_date": i18n.header.date(),
        "reminder_date": reminder.date,
        "header_time": i18n.header.time(),
        "reminder_time": get_time_str(reminder.time),
        "header_period": i18n.header.period(),
        "reminder_period": get_period_str(reminder.period, i18n.not_.periodically()),
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
    **kwargs,
):
    return {
        "amount_passed": i18n.amount.passed(),
        "amount": len(REMINDERS),
        "button_main_menu": i18n.button.main.menu(),
        "reminders": REMINDERS,
    }
