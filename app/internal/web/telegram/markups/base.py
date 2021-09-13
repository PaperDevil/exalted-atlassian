from aiogram.types import InlineKeyboardMarkup


class BaseMarkup:
    keyboard: list = []

    @classmethod
    def get_markup(cls) -> InlineKeyboardMarkup:
        keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup()
        for button in cls.keyboard:
            keyboard.add(button)
        return keyboard
