import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
from fluentogram import TranslatorHub
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from core import Settings
from bot.dialogs import setup_dialogs
from bot.utils.i18n import create_translator_hub
from bot.middlewares.i18n import TranslatorRunnerMiddleware
from bot.middlewares.session import DbSessionMiddleware
from bot.middlewares.yadisk import YaDiskMiddleware
from bot.handlers.commands import router

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] #%(levelname)-8s %(filename)s:%(lineno)d - %(name)s - %(message)s",
)

logger = logging.getLogger(__name__)


async def main() -> None:
    settings = Settings()

    engine = create_async_engine(settings.pg_dns)

    async with engine.begin() as conn:
        await conn.execute(text("SELECT 1"))

    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher(storage=MemoryStorage())

    translator_hub: TranslatorHub = create_translator_hub()

    dp.include_router(router)
    setup_dialogs(dp)

    Sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
    dp.update.outer_middleware(YaDiskMiddleware(settings.yandex_key))
    dp.update.outer_middleware(DbSessionMiddleware(Sessionmaker))
    dp.update.middleware(TranslatorRunnerMiddleware())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, _translator_hub=translator_hub)


if __name__ == "__main__":
    asyncio.run(main())
