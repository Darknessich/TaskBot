from aiogram_dialog import Dialog

from . import windows

new_reminder = Dialog(
    windows.start_window,
    windows.set_description_window,
    windows.set_date_window,
    windows.set_time_window,
    windows.set_period_window,
    windows.set_files_window,
)
