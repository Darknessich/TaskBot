from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.kbd import Button

from bot.dialogs.start.getters import get_start
from bot.states.start import StartSG

start_dialog = Dialog(
    Window(
        Format("{start_answer}"),
        Button(Format("{button_new_reminder}"), id="new_reminder"),
        Button(Format("{button_list_reminders}"), id="list_reminders"),
        Button(Format("{button_list_passed}"), id="list_passed"),
        Button(Format("{button_lang_setup}"), id="lang_setup"),
        getter=get_start,
        state=StartSG.start,
    ),
)
