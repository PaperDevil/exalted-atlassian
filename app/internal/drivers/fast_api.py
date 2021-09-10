import sys

from loguru import logger
from fastapi import FastAPI

from app.conf.server import (
    DEBUG, TITLE_API,
    DESCRIPTION_API, VERSION_API,
    TELEGRAM_TOKEN
)
from app.internal.drivers.telegram_driver import TelegramBotAPI
from app.internal.web.api.general import general_router


class FastAPIServer:

    @staticmethod
    def get_app() -> FastAPI:
        logger.add(sys.stderr, level='INFO')

        app = FastAPI(
            debug=DEBUG,
            title=TITLE_API,
            description=DESCRIPTION_API,
            version=VERSION_API,
            docs_url='/swagger',
            openapi_url='/openapi.json'
        )

        app.include_router(general_router)

        @app.on_event('startup')
        async def init_telegram_api():
            TelegramBotAPI.init_bot_api(TELEGRAM_TOKEN)

        return app
