from aiogram.types import InlineKeyboardMarkup


class BaseMarkup:
    keyboard: list = []

    def get_markup(self) -> InlineKeyboardMarkup:
        keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup()
        for button in self.keyboard:
            keyboard.add(button)
        return keyboard
