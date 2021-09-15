from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from app.conf.server import TELEGRAM_BOT_ADDRESS
from app.internal.drivers.telegram_driver import TelegramBotAPI
from app.internal.logic.entities.db.user import User
from app.internal.logic.services.user import UserService
from app.internal.web.telegram.markups.menu import MenuKeyboardMarkup

user_router = APIRouter(prefix='/user', tags=['User API'])


@user_router.get('/auth/{user_id}')
async def bitbucket_auth(
        user_id: int,
        state: str, code: str):
    await UserService.auth_bitbucket(user_id, state, code)
    user: User = await UserService.get_user_by_id(user_id)
    bot = TelegramBotAPI.get_bot()
    await bot.send_message(
        chat_id=user.telegram_id,
        text="You now have access to the bot functionality!",
        reply_markup=MenuKeyboardMarkup().get_markup()
    )
    return RedirectResponse(TELEGRAM_BOT_ADDRESS)
