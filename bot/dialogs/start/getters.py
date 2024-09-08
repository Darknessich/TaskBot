from typing import TYPE_CHECKING

from aiogram import html
from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner


async def get_start(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    event_from_user: User,
    **kwargs,
) -> dict[str, str]:
    username = html.quote(event_from_user.full_name)
    return {
        "start_answer": i18n.start.answer(username=username),
        "button_new_reminder": i18n.button.new.reminder(),
        "button_list_reminders": i18n.button.list.reminders(),
        "button_list_passed": i18n.button.list.passed(),
        "button_lang_setup": i18n.button.lang.setup(),
    }
