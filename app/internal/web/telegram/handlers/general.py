from app.internal.web.telegram.handlers.callback import process_menu
from app.internal.web.telegram.handlers.commands import start, about
from app.internal.web.telegram.handlers.callback import get_menu

general_handler: dict = {
    'message': [
        {'callback': start, 'commands': ['start']},
        {'callback': about, 'commands': ['about']},
        {'callback': get_menu, 'commands': ['menu']}
    ],
    'callback': [
        {'callback': process_menu}
    ]
}
