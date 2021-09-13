import time
from typing import Optional

from aiogram import Bot, Dispatcher
from aiogram import types

from app.conf.server import HTTPS_HOST_ADDRESS


class TelegramBotAPI:
    __bot: Optional[Bot] = None
    __dispatcher: Optional[Dispatcher] = None

    @classmethod
    async def init_bot_api(cls, token: str, handlers: dict) -> None:
        cls.__bot = Bot(token)
        cls.__dispatcher = Dispatcher(cls.__bot)
        cls.include_handlers(handlers)
        await cls.__bot.delete_webhook()
        await cls.__bot.get_updates()
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
    def include_handlers(cls, handlers: dict[str:list]):
        for group_name, group in handlers.items():
            if group_name == 'message':
                for handler in group:
                    cls.__dispatcher.register_message_handler(
                        callback=handler.get('callback'),
                        commands=handler.get('commands')
                    )
            elif group_name == 'callback':
                for handler in group:
                    cls.__dispatcher.register_callback_query_handler(
                        callback=handler.get('callback'),
                        text=handler.get('text')
                    )
            else:
                raise TypeError(f"Type of handler not supported! {group}")

    @classmethod
    async def update(cls, data: dict):
        Bot.set_current(cls.get_bot())
        await cls.__dispatcher.process_update(
            update=types.Update(**data)
        )

    @classmethod
    async def _set_webhook(cls) -> None:
        await cls.__bot.set_webhook(HTTPS_HOST_ADDRESS, drop_pending_updates=True)
