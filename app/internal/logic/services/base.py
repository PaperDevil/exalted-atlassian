from telegram.ext import Updater

from app.internal.drivers.telegram_driver import TelegramBotAPI


class BaseService:
    def __init__(self):
        self.tg: Updater = TelegramBotAPI.get_updater()
