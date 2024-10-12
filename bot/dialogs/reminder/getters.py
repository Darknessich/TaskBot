from typing import TYPE_CHECKING

from aiogram.types import Document
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

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


async def get_new_reminder(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    **kwargs,
) -> dict:
    ctx = dialog_manager.current_context()

    if dialog_manager.start_data and dialog_manager.start_data.get("reminder"):
        ctx.dialog_data.update(reminder=dialog_manager.start_data.get("reminder"))

    if not ctx.dialog_data.get("reminder"):
        ctx.dialog_data.update(
            reminder={
                "description": None,
                "date": None,
                "time": 0,
                "period": 0,
                "files": [],
            }
        )
    reminder: dict = ctx.dialog_data.get("reminder")
    description = reminder.get("description")
    date = reminder.get("date")
    time: int = reminder.get("time")
    period: int = reminder.get("period")
    files: list[Document] = reminder.get("files")

    return {
        "header_description": i18n.header.description(),
        "reminder_description": "" if not description else description,
        "header_date": i18n.header.date(),
        "reminder_date": "????-??-??" if not date else date,
        "header_time": i18n.header.time(),
        "reminder_time": get_time_str(time),
        "header_period": i18n.header.period(),
        "reminder_period": get_period_str(period, i18n.not_.periodically()),
        "header_files": i18n.header.files(),
        "reminder_files": get_files_str(files),
        "button_set_description": i18n.button.set.description(),
        "button_set_date": i18n.button.set.date(),
        "button_set_time": i18n.button.set.time(),
        "button_set_period": i18n.button.set.period(),
        "button_set_files": i18n.button.set.files(),
        "button_save": i18n.button.save(),
        "button_cancel": i18n.button.cancel(),
    }


async def get_description_window_data(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    **kwargs,
):
    ctx = dialog_manager.current_context()
    reminder: dict = ctx.dialog_data.get("reminder")
    description: str | None = reminder.get("description")

    return {
        "enter_description": i18n.enter.description(),
        "current_description": i18n.current.description(),
        "reminder_description": "" if not description else description,
        "button_back": i18n.button.back(),
    }


async def get_date_window_data(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    **kwargs,
):
    ctx = dialog_manager.current_context()
    reminder: dict = ctx.dialog_data.get("reminder")
    return {
        "enter_date": i18n.enter.date(),
        "current_date": i18n.current.date(),
        "reminder_date": reminder.get("date"),
        "button_back": i18n.button.back(),
    }


async def get_time_window_data(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    **kwargs,
):
    ctx = dialog_manager.current_context()
    reminder: dict = ctx.dialog_data.get("reminder")
    time: int = reminder.get("time")

    hours = time // 60
    minutes = time % 60

    return {
        "enter_time": i18n.enter.time(),
        "current_time": i18n.current.time(),
        "reminder_time": get_time_str(time),
        "button_apply": i18n.button.apply(),
        "reminder_hours": f"{hours:02}",
        "reminder_minutes": f"{minutes:02}",
    }


async def get_period_window_data(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    **kwargs,
):
    ctx = dialog_manager.current_context()
    reminder: dict = ctx.dialog_data.get("reminder")
    period: int = reminder.get("period")

    days = period // 1440
    hours = (period // 60) % 24
    minutes = period % 60

    return {
        "enter_period": i18n.enter.time(),
        "current_period": i18n.current.time(),
        "reminder_period": get_period_str(period, i18n.not_.periodically()),
        "button_apply": i18n.button.apply(),
        "button_without_period": i18n.button.without.period(),
        "reminder_days": f"{days:03}",
        "reminder_hours": f"{hours:02}",
        "reminder_minutes": f"{minutes:02}",
    }


async def get_files_window_data(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    **kwargs,
):
    ctx = dialog_manager.current_context()
    reminder: dict = ctx.dialog_data.get("reminder")
    files = reminder.get("files")

    return {
        "enter_files": i18n.enter.files(),
        "button_apply": i18n.button.apply(),
        "files": files,
    }
