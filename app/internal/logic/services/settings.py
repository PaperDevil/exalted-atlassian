from typing import Optional

from app.internal.logic.dao.settings import SettingsDao
from app.internal.logic.entities.db.settings import Settings
from app.internal.logic.entities.db.user import User
from app.internal.logic.services.base import BaseService


class SettingsService(BaseService):
    @staticmethod
    async def create_user_default(user_id: int) -> Optional[Settings]:
        settings: Settings = await SettingsDao().add(Settings(
            notifications=True, user=User(id=user_id)
        ))
        return settings

    @staticmethod
    async def get_by_user_id(user_id: int) -> Optional[Settings]:
        settings: Settings = await SettingsDao().get_by_user_id(user_id)
        return settings

    @staticmethod
    async def update(id: int, settings: Settings) -> Optional[Settings]:
        settings: Settings = await SettingsDao().update(id, settings)
        return settings
