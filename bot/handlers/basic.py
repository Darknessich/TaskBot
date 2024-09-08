from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message
from fluentogram import TranslatorRunner

router = Router()


@router.message(CommandStart())
async def proccess_start_command(message: Message, i18n: TranslatorRunner):
    username = message.from_user.full_name
    await message.answer(text=i18n.start.answer(username=username))
