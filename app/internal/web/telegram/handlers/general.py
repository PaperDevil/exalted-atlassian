from telegram.ext import Handler, CommandHandler

from app.internal.web.telegram.handlers.commands import start, about

general_handler: list[Handler] = [
    CommandHandler('start', start),
    CommandHandler('about', about)
]
