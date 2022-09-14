from aiogram.types import InlineKeyboardButton

from app.internal.logic.entities.common.workspace import BitbucketWorkspace
from app.internal.web.telegram.markups.base import BaseMarkup


class WorkspacesKeyboard(BaseMarkup):
    def __init__(self, workspaces: list[BitbucketWorkspace]):
        self.keyboard = []
        for workspace in workspaces:
            self.keyboard.append(InlineKeyboardButton(
                text=f"{workspace.name} 👥",
                callback_data=f"workspaces:detail?slug={workspace.slug}"
            ))
        self.keyboard.append(InlineKeyboardButton(
            text="Close ❌", callback_data="menu?"
        ))


class WorkspaceDetailKeyboard(BaseMarkup):
    def __init__(self, workspace: BitbucketWorkspace):
        self.keyboard = []
        self.keyboard.append(InlineKeyboardButton(
            text="Repositories 🌐", callback_data=f"repos:wsrp?slug={workspace.slug}"
        ))
        self.keyboard.append(InlineKeyboardButton(
            text="Members 👥", callback_data=f"workspaces:memb?slug={workspace.slug}"
        ))
        self.keyboard.append(InlineKeyboardButton(
            text="Menu ❌", callback_data="menu?"
        ))
