from aiogram_dialog import Dialog

from . import windows

reminders_list = Dialog(
    windows.reminders_list_window,
    windows.reminder_window,
)
passed_list = Dialog(
    windows.passed_list_window,
    windows.passed_window,
)
