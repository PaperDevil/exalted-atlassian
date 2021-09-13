from aiogram.types import InlineKeyboardButton

from app.internal.logic.entities.common.workspace import BitbucketWorkspace
from app.internal.web.telegram.markups.base import BaseMarkup


class WorkspacesKeyboard(BaseMarkup):
    def __init__(self, workspaces: list[BitbucketWorkspace]):
        self.keyboard = []
        for workspace in workspaces:
            self.keyboard.append(InlineKeyboardButton(
                text=f"{workspace.name} 👥",
                callback_data=f"workspaces:detail?id={workspace.uuid}"
            ))
