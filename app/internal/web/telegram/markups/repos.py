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
            text="Set Webhook 💡", callback_data=f"repos:wh?name={repo.full_name}"
        ))
        self.keyboard.append(InlineKeyboardButton(
            text="Settings 🔧", callback_data="repos:wh?"
        ))


class RepoWebhookKeyboard(BaseMarkup):
    def __init__(self, full_name: str):
        self.keyboard = []
        self.keyboard.append(InlineKeyboardButton(
            text="Site 🌐", url=f"https://bitbucket.org/{full_name}/admin/webhooks",
        ))
        self.keyboard.append(InlineKeyboardButton(
            text="Close ❌", callback_data="repos?",
        ))
