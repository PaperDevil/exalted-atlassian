from aiogram import Bot
from app.internal.drivers.telegram_driver import TelegramBotAPI


class BaseService:
    def __init__(self):
        self.tg: Bot = TelegramBotAPI.get_bot()
