from app.external.utils.config import ConfigUtils


DB_PORT = ConfigUtils.env('DB_PORT', str)
DB_HOST = ConfigUtils.env('DB_HOST', str)
DB_PASSWORD = ConfigUtils.env('DB_PASSWORD', str)
DB_NAME = ConfigUtils.env('DB_NAME', str)
DB_USER = ConfigUtils.env('DB_USER', str)
