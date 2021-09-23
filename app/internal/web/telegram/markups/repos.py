from aiogram.types import InlineKeyboardButton

from app.internal.logic.entities.common.repository import BitbucketRepository
from app.internal.web.telegram.markups.base import BaseMarkup


class ReposKeyboard(BaseMarkup):
    def __init__(self, repos: list[BitbucketRepository]):
        self.keyboard = []
        for repo in repos:
            self.keyboard.append(InlineKeyboardButton(
                text=f'{repo.full_name} 🌐',
                callback_data=f"repos:detail?id={repo.uuid}"
            ))


class RepoDetailKeyboard(BaseMarkup):
    def __init__(self, repo: BitbucketRepository):
        self.keyboard = []
        self.keyboard.append(InlineKeyboardButton(
            text="Site 🌐", url=repo.website,
        ))
        self.keyboard.append(InlineKeyboardButton(
            text="Set Webhook 💡", callback_data=f"repos:wh?id={repo.uuid}"
        ))
        self.keyboard.append(InlineKeyboardButton(
            text="Settings 🔧", callback_data=f"repos:settings?id={repo.uuid}"
        ))
        self.keyboard.append(InlineKeyboardButton(
            text="Back 🔙", callback_data="repos?"
        ))


class RepoWebhookKeyboard(BaseMarkup):
    def __init__(self, repo: BitbucketRepository):
        self.keyboard = []
        self.keyboard.append(InlineKeyboardButton(
            text="Setup ⏫", callback_data=f"repos:swh?id={repo.uuid}"
        ))
        self.keyboard.append(InlineKeyboardButton(
            text="Site 🌐", url=f"https://bitbucket.org/{repo.full_name}/admin/webhooks",
        ))
        self.keyboard.append(InlineKeyboardButton(
            text="Close ❌", callback_data="repos?",
        ))


class RepoJustCloseKeyboard(BaseMarkup):
    def __init__(self):
        self.keyboard = []
        self.keyboard.append(InlineKeyboardButton(
            text="Close ❌", callback_data="repos?"
        ))


class RepoSettingsKeyboard(BaseMarkup):
    def __init__(self, repo: BitbucketRepository):
        self.keyboard = []
        self.keyboard.append(InlineKeyboardButton(
            text="Branches", callback_data=f"repos:branches?id={repo.uuid}"
        ))
        self.keyboard.append(InlineKeyboardButton(
            text="Close ❌", callback_data=f"repos:settings?id={repo.uuid}"
        ))
