from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.kbd import Button

from . import handlers, getters
from bot.states.start import StartSG

start_window = Window(
    Format("{start_answer}"),
    Button(
        Format("{button_new_reminder}"),
        id="new_reminder",
        on_click=handlers.go_new_reminder,
    ),
    Button(
        Format("{button_list_reminders}"),
        id="list_reminders",
        on_click=handlers.go_reminders_list,
    ),
    Button(
        Format("{button_list_passed}"),
        id="list_passed",
        on_click=handlers.go_passed_list,
    ),
    # Button(
    #     Format("{button_lang_setup}"),
    #     id="lang_setup",
    #     on_click=handlers.go_setup_language,
    # ),
    getter=getters.get_start,
    state=StartSG.start,
)
