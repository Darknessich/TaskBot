import operator
from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.kbd import Select, Cancel, Back, Button, ScrollingGroup

from bot.states.lists import RemindersListSG, PassedListSG
from . import handlers, getters

reminders_list_window = Window(
    Format("{amount_reminders}: {amount}"),
    ScrollingGroup(
        Select(
            Format("{item.description}"),
            id="select_reminder",
            item_id_getter=operator.attrgetter("id"),
            items="reminders",
            on_click=handlers.selected_reminder,
        ),
        id="scrolling_reminders",
        width=1,
        height=5,
    ),
    Cancel(Format("{button_main_menu}")),
    state=RemindersListSG.list,
    getter=getters.get_reminder_list_window,
)

reminder_window = Window(
    Format("{header_description}: {reminder_description}"),
    Format("{header_date}: {reminder_date}"),
    Format("{header_time}: {reminder_time}"),
    Format("{header_period}: {reminder_period}"),
    Format("{header_files}:\n{reminder_files}"),
    Button(
        Format("{button_set_reminder}"),
        id="button_set_reminder",
        on_click=handlers.on_set_reminder,
    ),
    Button(
        Format("{button_done}"),
        id="button_done_reminder",
        on_click=handlers.on_done_reminder,
    ),
    Button(
        Format("{button_delete}"),
        id="button_delte_reminder",
        on_click=handlers.on_delete_reminder,
    ),
    Back(Format("{button_back}")),
    state=RemindersListSG.reminder,
    getter=getters.get_reminder_window,
)

passed_list_window = Window(
    Format("{amount_passed}: {amount}"),
    ScrollingGroup(
        Select(
            Format("{item.description}"),
            id="select_reminder",
            item_id_getter=operator.attrgetter("id"),
            items="reminders",
            on_click=handlers.selected_reminder,
        ),
        id="scrolling_passed",
        width=1,
        height=5,
    ),
    Cancel(Format("{button_main_menu}")),
    state=PassedListSG.list,
    getter=getters.get_passed_list_window,
)

passed_window = Window(
    Format("{header_description}: {reminder_description}"),
    Format("{header_date}: {reminder_date}"),
    Format("{header_time}: {reminder_time}"),
    Format("{header_period}: {reminder_period}"),
    Format("{header_files}:\n{reminder_files}"),
    Button(
        Format("{button_set_passed}"),
        id="button_set_passed",
        on_click=handlers.on_set_passed,
    ),
    Button(
        Format("{button_delete}"),
        id="button_delte_passed",
        on_click=handlers.on_delete_reminder,
    ),
    Back(Format("{button_back}")),
    state=PassedListSG.reminder,
    getter=getters.get_reminder_window,
)
