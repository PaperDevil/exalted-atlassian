from typing import Optional

from telegram.ext import Updater, Dispatcher


class TelegramBotAPI:
    __updater: Optional[Updater] = None
    __dispatcher: Optional[Dispatcher] = None

    @classmethod
    def init_bot_api(cls, token) -> None:
        cls.__updater = Updater(token, use_context=True, workers=1)
        cls.__dispatcher = cls.__updater.dispatcher

    @classmethod
    def get_updater(cls) -> Updater:
        return cls.__updater
