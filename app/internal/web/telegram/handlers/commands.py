from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.external.logic.services import BitbucketOAuth2Service
from app.internal.drivers.cache_driver import CacheDriver
from app.internal.logic.entities.db.user import User
from app.internal.logic.services.user import UserService
from app.internal.web.telegram.markups.menu import MenuKeyboardMarkup


async def start(event: types.Message) -> types.Message:
    user: User = await UserService.get_user_by_telegram_id(event.from_user.id)
    if user and CacheDriver.exist(user.id):
        access_token = await CacheDriver.get_field(user.id, 'access_token')
        if access_token:
            return await event.answer(
                text=f"You now have access to the bot functionality!",
                reply_markup=MenuKeyboardMarkup.get_markup()
            )
    await register(event)


async def register(event: types.Message) -> None:
    user: User = await UserService.create_user(str(event.from_user.id))
    auth_url: str = await BitbucketOAuth2Service.get_oath_url(user.id)
    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Authorize", url=auth_url))
    await event.bot.send_photo(
        event.from_user.id,
        photo='https://cdn.javarush.ru/images/article/5a370e86-a6bf-4522-b12f-67ab72e61b88/800.jpeg',
        reply_markup=keyboard,
        caption=f'Before you start using the bot, you need to authorize the bot in your bitbucket account.'
    )


async def about(event: types.Message) -> None:
    await event.reply('This bot is made for doing things. ')
