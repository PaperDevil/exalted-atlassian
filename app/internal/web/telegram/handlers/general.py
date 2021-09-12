from app.internal.web.telegram.handlers.commands import start, about

general_handler: list[dict] = [
    {'callback': start, 'commands': ['start']},
    {'callback': about, 'commands': ['about']}
]
