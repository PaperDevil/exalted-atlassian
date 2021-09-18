from typing import Optional

from asyncpg import UniqueViolationError
from sqlalchemy import select

from app.internal.logic.dao.base import BaseDao
from app.internal.logic.deserializers.settings import SettingsDeserializer
from app.internal.logic.entities.db.settings import Settings
from app.schema.meta import settings_table


class SettingsDao(BaseDao):
    deserializer = SettingsDeserializer
    default_rows = [
        settings_table.c.id.label('settings_id'),
        settings_table.c.created_at.label('settings_created_at'),
        settings_table.c.edited_at.label('settings_updated_at'),
        settings_table.c.notifications.label('settings_notifications'),
        settings_table.c.user_id.label('user_id')
    ]

    async def add(self, settings: Settings) -> Settings:
        query = settings_table.insert().values(
            notifications=settings.notifications,
            user_id=settings.user.id
        ).returning(settings_table.c.id)

        async with self.connection as conn:
            try:
                settings_id = await conn.fetchval(query)
            except UniqueViolationError as exc:
                raise

        settings.id = settings_id
        return settings

    async def get_by_id(self, id: int) -> Optional[Settings]:
        query = select(self.default_rows).select_from(settings_table).where(
            settings_table.c.id == id
        )
        return await self.get_object_by_field(query)

    async def get_by_user_id(self, user_id: int) -> Optional[Settings]:
        query = select(self.default_rows).select_from(settings_table).where(
            settings_table.c.user_id == user_id
        )
        return await self.get_object_by_field(query)

    async def update(self, id: int, settings: Settings) -> Optional[Settings]:
        query = settings_table.update().values(
            notifications=settings.notifications
        )
        return await self.get_object_by_field(query)
