from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.external.logic.services import BitbucketOAuth2Service
from app.internal.logic.entities.db.user import User
from app.internal.logic.services.user import UserService


async def start(event: types.Message) -> None:
    await register(event)


async def register(event: types.Message) -> None:
    user: User = await UserService.create_user(str(event.from_user.id))
    auth_url: str = await BitbucketOAuth2Service.get_oath_url(user.id)
    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Authorize", url=auth_url))
    await event.answer(
        f'Before you start using the bot, you need to authorize the bot in your bitbucket account.',
        reply_markup=keyboard
    )


async def about(event: types.Message) -> None:
    await event.reply('This bot is made for doing things. ')
