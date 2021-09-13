from app.external.utils.config import ConfigUtils

CONSUMER_KEY = ConfigUtils.env('OAUTH_CONSUMER_KEY', str)
CONSUMER_SECRET = ConfigUtils.env('OAUTH_CONSUMER_SECRET', str)
