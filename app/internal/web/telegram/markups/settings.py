from aiogram.types import InlineKeyboardButton

from app.internal.logic.entities.db.settings import Settings
from app.internal.web.telegram.markups.base import BaseMarkup


class SettingsMenuKeyboard(BaseMarkup):
    def __init__(self, settings: Settings):
        self.keyboard = []
        self.keyboard.append(InlineKeyboardButton(
                text=f'Notifications {"🟢" if settings.notifications else "🔴"}',
                callback_data=f"settings:notify?"
            ))
        self.keyboard.append(InlineKeyboardButton(
            text="Close ❌", callback_data="menu?"
        ))
