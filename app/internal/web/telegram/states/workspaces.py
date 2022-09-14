from aiogram import types
import aiogram.utils.markdown as fmt

from app.external.drivers.bitbucket import BitbucketDriver
from app.internal.web.telegram.markups.workspaces import WorkspacesKeyboard, WorkspaceDetailKeyboard
from app.internal.web.telegram.states.base import BaseStates
from app.internal.logic.entities.db.user import User


class WorkspacesStates(BaseStates):
    def __init__(self):
        self.handlers = {
            '-': self.get_workspaces,
            'detail': self.workspace_detail
        }
        self.payload = {}

    @staticmethod
    async def get_workspaces(event: types.CallbackQuery, user: User, driver: BitbucketDriver, payload: dict):
        workspaces = await driver.get_workspaces()
        keyboard = WorkspacesKeyboard(workspaces).get_markup()
        await event.message.edit_text(text=fmt.text(
            "Here you can find workspaces, where you have permissions."
        ))
        await event.message.edit_reply_markup(reply_markup=keyboard)

    @staticmethod
    async def workspace_detail(event: types.CallbackQuery, user: User, driver: BitbucketDriver, payload: dict):
        workspace = await driver.get_workspace(payload.get('slug'))
        keyboard = WorkspaceDetailKeyboard(workspace).get_markup()
        await event.message.edit_text(text=fmt.text(
            fmt.text(f"{workspace.name} Workspace:")
        ))
        await event.message.edit_reply_markup(reply_markup=keyboard)
