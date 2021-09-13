from aiogram import types

from app.external.drivers.bitbucket import BitbucketDriver
from app.internal.drivers.cache_driver import CacheDriver
from app.internal.logic.services.user import UserService
from app.internal.web.telegram.markups.workspaces import WorkspacesKeyboard
from app.internal.web.telegram.states.base import BaseStates


class WorkspacesStates(BaseStates):
    def __init__(self):
        self.handlers = {
            '-': self.get_workspaces,
            'get_detail_workspace': self.get_detail_workspace
        }
        self.payload = {}

    @staticmethod
    async def get_workspaces(event: types.CallbackQuery, vars: dict):
        user = await UserService.get_user_by_telegram_id(event.from_user.id)
        access_token = await CacheDriver.get_field(user.id, 'access_token')
        workspaces = await BitbucketDriver.get_workspaces(access_token['access_token'])
        keyboard = WorkspacesKeyboard(workspaces).get_markup()
        await event.bot.send_message(event.from_user.id, text="It's workspaces", reply_markup=keyboard)

    @staticmethod
    async def get_detail_workspace(event: types.CallbackQuery, vars: dict):
        await event.message.answer(text=f"{vars['id']} type /menu to go menu!")
