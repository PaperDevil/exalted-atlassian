from aiogram import types, Bot

from app.internal.logic.entities.db.user import User
from app.internal.logic.services.user import UserService
from app.internal.drivers.telegram_driver import TelegramBotAPI


async def start(event: types.Message) -> None:
    user: User = await UserService.create_user(str(event.from_user.id))
    Bot.set_current(TelegramBotAPI.get_bot())
    await event.reply(f'yours user_id is {user.id}')


async def about(event: types.Message) -> None:
    await event.reply('This bot is made for doing things. ')
