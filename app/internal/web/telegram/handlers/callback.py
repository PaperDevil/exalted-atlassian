from aiogram import types, Dispatcher

from app.external.utils.handler_routing import parse_button_route
from app.internal.drivers.telegram_driver import TelegramBotAPI
from app.internal.web.telegram.markups.menu import MenuKeyboardMarkup
from app.internal.web.telegram.states.repos import ReposStates

dp: Dispatcher = TelegramBotAPI.get_dispatcher()


async def get_menu(event: types.Message):
    await event.bot.send_message(
        event.from_user.id,
        text=f"You now have access to the bot functionality!",
        reply_markup=MenuKeyboardMarkup().get_markup()
    )


async def process_menu(event: types.CallbackQuery):
    payload = parse_button_route(event.data)
    if payload['route']['0'] == 'repos':
        return await ReposStates().process(event)
    if payload['route']['0'] == 'settings':
        pass
    await event.message.edit_text(text=f"This option has coming soon...")
