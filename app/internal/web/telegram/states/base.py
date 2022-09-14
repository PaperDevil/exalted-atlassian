from aiogram import types

from app.external.drivers.bitbucket import BitbucketDriver
from app.external.utils.handler_routing import parse_button_route
from app.internal.logic.entities.db.user import User
from app.internal.logic.services.user import UserService


class BaseStates:
    handlers = {}
    payload = {}

    user: User
    driver: BitbucketDriver

    @classmethod
    async def create(cls, user_telegram_id):
        self = cls()
        self.user = await UserService.get_user_by_telegram_id(user_telegram_id)
        await self.user.get_session()
        self.driver = BitbucketDriver(await self.user.access_token)
        return self

    async def process(self, event: types.CallbackQuery):
        self.payload = parse_button_route(event.data)
        if len(self.payload['route']) == 1:
            await self.handlers['-'](event, self.user, self.driver, self.payload['vars'])
        else:
            func: str = self.payload['route']['1']
            if func not in self.handlers:
                return await event.bot.send_message(
                    event.from_user.id, text="This option has coming soon..."
                )
            await self.handlers[func](event, self.user, self.driver, self.payload['vars'])
