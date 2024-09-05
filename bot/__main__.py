import asyncio
from aiogram import Bot, Dispatcher
from bot.core import Settings


async def main() -> None:
    settings = Settings()
    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
