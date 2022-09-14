from aiogram import types, Dispatcher
from loguru import logger

from app.external.utils.handler_routing import parse_button_route
from app.internal.drivers.telegram_driver import TelegramBotAPI
from app.internal.web.telegram.markups.menu import MenuKeyboardMarkup
from app.internal.web.telegram.states.repos import ReposStates
from app.internal.web.telegram.states.settings import SettingsStates
from app.internal.web.telegram.states.workspaces import WorkspacesStates
from app.internal.web.telegram.texts.errors import ERROR_CAUGHT_CASE

dp: Dispatcher = TelegramBotAPI.get_dispatcher()


async def get_menu(event: types.Message):
    await event.bot.send_message(
        event.from_user.id,
        text=f"You now have access to the bot functionality!",
        reply_markup=MenuKeyboardMarkup().get_markup()
    )


async def update_menu(event: types.Message):
    await event.edit_text(
        text=f"You now have access to the bot functionality!",
        reply_markup=MenuKeyboardMarkup().get_markup()
    )


async def process_menu(event: types.CallbackQuery):
    payload = parse_button_route(event.data)
    try:
        if payload['route']['0'] == 'repos':
            states = await ReposStates.create(event.from_user.id)
            return await states.process(event)
        if payload['route']['0'] == 'settings':
            states = await SettingsStates.create(event.from_user.id)
            return await states.process(event)
        if payload['route']['0'] == 'workspaces':
            states = await WorkspacesStates.create(event.from_user.id)
            return await states.process(event)
        if payload['route']['0'] == 'menu':
            return await update_menu(event.message)
    except Exception as exc:
        await event.message.answer(ERROR_CAUGHT_CASE)
        logger.exception(exc)
    await event.message.edit_text(text=f"This option has coming soon...")
