import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from fluentogram import TranslatorHub

from bot.core import Settings
from bot.dialogs import setup_dialogs
from bot.utils.i18n import create_translator_hub
from bot.middlewares.i18n import TranslatorRunnerMiddleware
from bot.handlers.commands import router

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] #%(levelname)-8s %(filename)s:%(lineno)d - %(name)s - %(message)s",
)

logger = logging.getLogger(__name__)


async def main() -> None:
    settings = Settings()
    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()

    translator_hub: TranslatorHub = create_translator_hub()

    dp.include_router(router)
    setup_dialogs(dp)

    dp.update.middleware(TranslatorRunnerMiddleware())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, _translator_hub=translator_hub)


if __name__ == "__main__":
    asyncio.run(main())
