from app.external.utils.config import ConfigUtils

DEBUG = ConfigUtils.env('DEBUG', bool)
ABOUT_TEXT = ConfigUtils.env('ABOUT_TEXT', str)