from asyncpg import Record

from app.internal.logic.deserializers.base import BaseDeserializer
from app.internal.logic.entities.db.user import User


class UserDeserializer(BaseDeserializer):
    @staticmethod
    def get_from_db(record: Record) -> User:
        return User(
            id=record.get('user_id'),
            created_at=record.get('user_created_at'),
            edited_at=record.get('user_edited_at'),
            telegram_id=record.get('user_telegram_id'),
            email=record.get('user_email')
        )