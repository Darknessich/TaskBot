import operator
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.kbd import (
    Button,
    Cancel,
    SwitchTo,
    Row,
    Group,
    ScrollingGroup,
    Select,
)

from bot.states.reminder import ReminderSG
from . import handlers

_YEAR = 525600
_DAY = 1440
_HOUR = 60
_MINUTES = 1
_SMALL_STEP = 1
_BIG_STEP = 5

start_window_kbd = Group(
    SwitchTo(
        Format("{button_set_description}"),
        id="button_set_description",
        state=ReminderSG.set_description,
    ),
    SwitchTo(
        Format("{button_set_date}"),
        id="button_set_date",
        state=ReminderSG.set_date,
    ),
    SwitchTo(
        Format("{button_set_time}"),
        id="button_set_time",
        state=ReminderSG.set_time,
    ),
    SwitchTo(
        Format("{button_set_period}"),
        id="button_set_period",
        state=ReminderSG.set_period,
    ),
    SwitchTo(
        Format("{button_set_files}"),
        id="button_set_files",
        state=ReminderSG.set_files,
    ),
    Button(
        Format("{button_save}"),
        id="button_save",
        on_click=handlers.on_save_reminder,
    ),
    Cancel(Format("{button_cancel}")),
)

set_time_window_kbd = Group(
    Row(
        Button(
            Const("+1"),
            id="hours_plus_one",
            on_click=handlers.TimeCallbackFactory(_SMALL_STEP, _DAY, _HOUR, "time"),
        ),
        Button(
            Const("+5"),
            id="hours_plus_five",
            on_click=handlers.TimeCallbackFactory(_BIG_STEP, _DAY, _HOUR, "time"),
        ),
        Button(
            Const("+1"),
            id="minutes_plus_one",
            on_click=handlers.TimeCallbackFactory(_SMALL_STEP, _DAY, _MINUTES, "time"),
        ),
        Button(
            Const("+5"),
            id="minutes_plus_five",
            on_click=handlers.TimeCallbackFactory(_BIG_STEP, _DAY, _MINUTES, "time"),
        ),
    ),
    Row(
        Button(Format("{reminder_hours}"), id="reminder_hours"),
        Button(Format("{reminder_minutes}"), id="reminder_minutes"),
    ),
    Row(
        Button(
            Const("-1"),
            id="hours_minus_one",
            on_click=handlers.TimeCallbackFactory(-_SMALL_STEP, _DAY, _HOUR, "time"),
        ),
        Button(
            Const("-5"),
            id="hours_minus_five",
            on_click=handlers.TimeCallbackFactory(-_BIG_STEP, _DAY, _HOUR, "time"),
        ),
        Button(
            Const("-1"),
            id="minutes_minus_one",
            on_click=handlers.TimeCallbackFactory(-_SMALL_STEP, _DAY, _MINUTES, "time"),
        ),
        Button(
            Const("-5"),
            id="minutes_minus_five",
            on_click=handlers.TimeCallbackFactory(-_BIG_STEP, _DAY, _MINUTES, "time"),
        ),
    ),
    SwitchTo(Format("{button_apply}"), id="button_apply", state=ReminderSG.start),
)

set_period_window_kbd = Group(
    Row(
        Button(
            Const("+1"),
            id="days_plus_one",
            on_click=handlers.TimeCallbackFactory(_SMALL_STEP, _YEAR, _DAY, "period"),
        ),
        Button(
            Const("+5"),
            id="days_plus_five",
            on_click=handlers.TimeCallbackFactory(_BIG_STEP, _YEAR, _DAY, "period"),
        ),
        Button(
            Const("+1"),
            id="hours_plus_one",
            on_click=handlers.TimeCallbackFactory(_SMALL_STEP, _YEAR, _HOUR, "period"),
        ),
        Button(
            Const("+5"),
            id="hours_plus_five",
            on_click=handlers.TimeCallbackFactory(_BIG_STEP, _YEAR, _HOUR, "period"),
        ),
        Button(
            Const("+1"),
            id="minutes_plus_one",
            on_click=handlers.TimeCallbackFactory(
                _SMALL_STEP, _YEAR, _MINUTES, "period"
            ),
        ),
        Button(
            Const("+5"),
            id="minutes_plus_five",
            on_click=handlers.TimeCallbackFactory(_BIG_STEP, _YEAR, _MINUTES, "period"),
        ),
    ),
    Row(
        Button(Format("{reminder_days}"), id="reminder_days"),
        Button(Format("{reminder_hours}"), id="reminder_hours"),
        Button(Format("{reminder_minutes}"), id="reminder_minutes"),
    ),
    Row(
        Button(
            Const("-1"),
            id="days_minus_one",
            on_click=handlers.TimeCallbackFactory(-_SMALL_STEP, _YEAR, _DAY, "period"),
        ),
        Button(
            Const("-5"),
            id="days_minus_five",
            on_click=handlers.TimeCallbackFactory(-_BIG_STEP, _YEAR, _DAY, "period"),
        ),
        Button(
            Const("-1"),
            id="hours_minus_one",
            on_click=handlers.TimeCallbackFactory(-_SMALL_STEP, _YEAR, _HOUR, "period"),
        ),
        Button(
            Const("-5"),
            id="hours_minus_five",
            on_click=handlers.TimeCallbackFactory(-_BIG_STEP, _YEAR, _HOUR, "period"),
        ),
        Button(
            Const("-1"),
            id="minutes_minus_one",
            on_click=handlers.TimeCallbackFactory(
                -_SMALL_STEP, _YEAR, _MINUTES, "period"
            ),
        ),
        Button(
            Const("-5"),
            id="minutes_minus_five",
            on_click=handlers.TimeCallbackFactory(
                -_BIG_STEP, _YEAR, _MINUTES, "period"
            ),
        ),
    ),
    SwitchTo(Format("{button_apply}"), id="button_apply", state=ReminderSG.start),
    SwitchTo(
        Format("{button_without_period}"),
        id="button_without_period",
        state=ReminderSG.start,
        on_click=handlers.on_period_delete,
    ),
)

set_files_window_kbd = Group(
    ScrollingGroup(
        Select(
            Format("Delete {item.file_name}"),
            id="select_files",
            item_id_getter=operator.attrgetter("file_unique_id"),
            items="files",
            on_click=handlers.on_delete_file,
        ),
        id="scrolling_files",
        width=1,
        height=5,
    ),
    SwitchTo(Format("{button_apply}"), id="button_apply", state=ReminderSG.start),
)
