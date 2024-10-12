from aiogram.types import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.kbd import SwitchTo, Calendar
from aiogram_dialog.widgets.input import TextInput, MessageInput

from bot.states.reminder import ReminderSG
from . import getters, handlers, keyboards

start_window = Window(
    Format("{header_description}: {reminder_description}"),
    Format("{header_date}: {reminder_date}"),
    Format("{header_time}: {reminder_time}"),
    Format("{header_period}: {reminder_period}"),
    Format("{header_files}:\n{reminder_files}"),
    keyboards.start_window_kbd,
    state=ReminderSG.start,
    getter=getters.get_new_reminder,
)

set_description_window = Window(
    Format("{enter_description}"),
    Format("{current_description}: {reminder_description}"),
    TextInput(id="input_description", on_success=handlers.on_description_input),
    SwitchTo(Format("{button_back}"), id="button_back", state=ReminderSG.start),
    state=ReminderSG.set_description,
    getter=getters.get_description_window_data,
)

set_date_window = Window(
    Format("{enter_date}"),
    Format("{current_date}: {reminder_date}"),
    Calendar(id="calendar_set_date", on_click=handlers.on_date_input),
    SwitchTo(Format("{button_back}"), id="button_back", state=ReminderSG.start),
    state=ReminderSG.set_date,
    getter=getters.get_date_window_data,
)

set_time_window = Window(
    Format("{enter_time}"),
    Format("{current_time}: {reminder_time}"),
    keyboards.set_time_window_kbd,
    state=ReminderSG.set_time,
    getter=getters.get_time_window_data,
)

set_period_window = Window(
    Format("{enter_period}"),
    Format("{current_period}: {reminder_period}"),
    keyboards.set_period_window_kbd,
    state=ReminderSG.set_period,
    getter=getters.get_period_window_data,
)

set_files_window = Window(
    Format("{enter_files}"),
    keyboards.set_files_window_kbd,
    MessageInput(
        handlers.on_document_input,
        content_types=ContentType.DOCUMENT,
    ),
    state=ReminderSG.set_files,
    getter=getters.get_files_window_data,
)
