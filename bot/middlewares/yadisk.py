from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from services.yadisk import YaDisk


class YaDiskMiddleware(BaseMiddleware):
    def __init__(self, yakey: str):
        super().__init__()
        self.yakey = yakey

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        data["yadisk"] = YaDisk(self.yakey)
        return await handler(event, data)
