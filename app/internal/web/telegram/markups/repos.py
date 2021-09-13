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
            text="Set Webhook 💡", callback_data="repos:wh?"
        ))
        self.keyboard.append(InlineKeyboardButton(
            text="Settings 🔧", callback_data="repos:wh?"
        ))
