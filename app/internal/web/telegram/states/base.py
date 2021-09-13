from aiogram import types

from app.external.utils.handler_routing import parse_button_route


class BaseStates:
    handlers = {}
    payload = {}

    async def process(self, event: types.CallbackQuery):
        self.payload = parse_button_route(event.data)
        if len(self.payload['route']) == 1:
            await self.handlers['-'](event, self.payload['vars'])
        else:
            func: str = self.payload['route']['1']
            if func not in self.handlers:
                return await event.bot.send_message(
                    event.from_user.id, text="This option has coming soon..."
                )
            await self.handlers[func](event, self.payload['vars'])