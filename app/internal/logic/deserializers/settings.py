from asyncpg import Record

from app.internal.logic.deserializers.base import BaseDeserializer
from app.internal.logic.deserializers.user import UserDeserializer
from app.internal.logic.entities.db.settings import Settings


class SettingsDeserializer(BaseDeserializer):
    @staticmethod
    def get_from_db(record: Record) -> Settings:
        return Settings(
            id=record.get('user_id'),
            created_at=record.get('user_created_at'),
            edited_at=record.get('user_edited_at'),
            notifications=record.get('settings_notifications'),
            user=UserDeserializer.get_from_db(record)
        )
