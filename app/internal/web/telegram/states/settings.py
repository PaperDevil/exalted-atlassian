from aiogram import types
import aiogram.utils.markdown as fmt

from app.internal.logic.entities.db.settings import Settings
from app.internal.logic.entities.db.user import User
from app.internal.logic.services.settings import SettingsService
from app.internal.web.telegram.markups.settings import SettingsMenuKeyboard
from app.internal.web.telegram.states.base import BaseStates


class SettingsStates(BaseStates):
    def __init__(self):
        self.handlers = {
            '-': self.show_settings_menu,
            'notify': self.notify
        }

    @staticmethod
    async def show_settings_menu(event: types.CallbackQuery, user: User, driver, payload: dict):
        settings: Settings = await SettingsService.get_by_user_id(user.id)
        keyboard = SettingsMenuKeyboard(settings).get_markup()
        await event.message.edit_text(
            text=fmt.text("To fine-tune the notification settings for each repository, you can select the repository and click 'Settings'."),
            reply_markup=keyboard
        )

    @staticmethod
    async def notify(event: types.CallbackQuery, user: User, driver, payload: dict):
        settings: Settings = await SettingsService.get_by_user_id(user.id)
        settings.notifications = not settings.notifications
        await SettingsService.update(settings.id, settings)
        await SettingsStates.show_settings_menu(event, user, driver, payload)
