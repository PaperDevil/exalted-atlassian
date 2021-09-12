import time
from typing import Optional

from telegram.error import RetryAfter
from telegram.ext import Updater, Dispatcher, Handler
from telegram import Update

from app.conf.server import HTTPS_HOST_ADDRESS


class TelegramBotAPI:
    __updater: Optional[Updater] = None
    __dispatcher: Optional[Dispatcher] = None

    @classmethod
    def init_bot_api(cls, token: str, handlers: list[Handler]) -> None:
        cls.__updater = Updater(token, use_context=True, workers=1)
        cls.__dispatcher = cls.__updater.dispatcher
        for handler in handlers:
            cls.include_handler(handler)
        cls._set_webhook()

    @classmethod
    def get_updater(cls) -> Updater:
        return cls.__updater

    @classmethod
    def update(cls, data: dict):
        cls.__dispatcher.process_update(
            update=Update.de_json(data, cls.__updater.bot)
        )

    @classmethod
    def include_handler(cls, handler: Handler) -> None:
        cls.__dispatcher.add_handler(handler)

    @classmethod
    def _set_webhook(cls) -> None:
        for _ in range(3):
            try:
                cls.__updater.bot.set_webhook(
                    url=HTTPS_HOST_ADDRESS
                )
                break
            except RetryAfter:
                time.sleep(3)
