import time
from typing import Optional

from aiogram import Bot, Dispatcher
from aiogram import types

from app.conf.server import HTTPS_HOST_ADDRESS


class TelegramBotAPI:
    __bot: Optional[Bot] = None
    __dispatcher: Optional[Dispatcher] = None

    @classmethod
    async def init_bot_api(cls, token: str, handlers: list) -> None:
        cls.__bot = Bot(token)
        cls.__dispatcher = Dispatcher(cls.__bot)
        for handler in handlers:
            cls.include_handler(handler['callback'], handler['commands'])
        await cls._set_webhook()

    @classmethod
    async def close_bot_api(cls):
        await cls.__bot.delete_webhook()

    @classmethod
    def get_dispatcher(cls) -> Dispatcher:
        return cls.__dispatcher

    @classmethod
    def get_bot(cls) -> Bot:
        return cls.__bot

    @classmethod
    def include_handler(cls, callback: callable, commands):
        cls.__dispatcher.register_message_handler(callback, commands=commands)

    @classmethod
    async def update(cls, data: dict):
        await cls.__dispatcher.process_update(
            update=types.Update(**data)
        )

    @classmethod
    async def _set_webhook(cls) -> None:
        await cls.__bot.set_webhook(HTTPS_HOST_ADDRESS)
