from app.external.utils.config import ConfigUtils

DEBUG = ConfigUtils.env('DEBUG', bool)
TITLE_API = ConfigUtils.env('TITLE_API', str)
DESCRIPTION_API = ''
VERSION_API = ConfigUtils.env('VERSION_API', str)

TELEGRAM_TOKEN = ConfigUtils.env('TELEGRAM_TOKEN', str)
CHANNEL_ID = ConfigUtils.env('CHANNEL_ID', str)

HTTPS_HOST_ADDRESS = ConfigUtils.env('HTTPS_HOST_ADDRESS', str)
TELEGRAM_BOT_ADDRESS = ConfigUtils.env('TELEGRAM_BOT_ADDRESS', str)
