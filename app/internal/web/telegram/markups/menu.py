from aiogram.types import InlineKeyboardButton

from app.internal.web.telegram.markups.base import BaseMarkup


class MenuKeyboardMarkup(BaseMarkup):
    keyboard = [
        InlineKeyboardButton(text="Repos 🌐", callback_data="repos"),
        InlineKeyboardButton(text="Settings 📦️", callback_data="settings")
    ]
