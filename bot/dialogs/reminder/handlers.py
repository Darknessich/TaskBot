import logging
from datetime import date
from aiogram_dialog.api.entities import ChatEvent
from aiogram.types import CallbackQuery, Message, Document
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, Calendar, Select
from aiogram_dialog.widgets.input import TextInput, MessageInput

from bot.states.reminder import ReminderSG


async def on_save_reminder(
    callback: CallbackQuery,
    widget: Button,
    dialog_manager: DialogManager,
):
    ctx = dialog_manager.current_context()
    reminder: dict = ctx.dialog_data.get("reminder")
    logging.log(logging.DEBUG, reminder)

    if not reminder.get("description"):
        await callback.answer("Заполните описание!")
        return

    if not reminder.get("date"):
        await callback.answer("Выберите дату!")
        return

    await callback.answer("Сохранено!")
    await dialog_manager.done()


async def on_description_input(
    message: Message,
    widget: TextInput,
    dialog_manager: DialogManager,
    description: str,
):
    ctx = dialog_manager.current_context()
    reminder: dict = ctx.dialog_data.get("reminder")
    reminder.update(description=description)
    await dialog_manager.switch_to(ReminderSG.start)


async def on_date_input(
    event: ChatEvent,
    widget: Calendar,
    dialog_manager: DialogManager,
    date: date,
):
    ctx = dialog_manager.current_context()
    reminder: dict = ctx.dialog_data.get("reminder")
    reminder.update(date=date)
    await dialog_manager.switch_to(ReminderSG.start)


class TimeCallbackFactory:
    def __init__(self, step: int, mod: int, factor: int, data: str):
        self.__step = step
        self.__mod = mod
        self.__factor = factor
        self.__data = data

    async def __call__(
        self,
        callback: CallbackQuery,
        widget: Button,
        dialog_manager: DialogManager,
    ):
        ctx = dialog_manager.current_context()
        reminder: dict = ctx.dialog_data.get("reminder")
        data: int = reminder.get(self.__data)
        new_data = (data + self.__step * self.__factor + self.__mod) % self.__mod
        reminder[self.__data] = new_data


async def on_period_delete(
    callback: CallbackQuery,
    widget: Button,
    dialog_manager: DialogManager,
):
    ctx = dialog_manager.current_context()
    reminder: dict = ctx.dialog_data.get("reminder")
    reminder["period"] = 0


async def on_document_input(
    message: Message,
    widget: MessageInput,
    dialog_manager: DialogManager,
):
    ctx = dialog_manager.current_context()
    reminder: dict = ctx.dialog_data.get("reminder")
    files: list = reminder.get("files")
    files.append(message.document)


async def on_delete_file(
    callback: CallbackQuery,
    widget: Select,
    dialog_manager: DialogManager,
    item_id: str,
):
    ctx = dialog_manager.current_context()
    reminder: dict = ctx.dialog_data.get("reminder")
    files: list[Document] = reminder.get("files")
    files = list(filter(lambda file: file.file_unique_id != item_id, files))
    reminder.update(files=files)
