from asyncpg import Record

from app.internal.logic.deserializers.base import BaseDeserializer
from app.internal.logic.deserializers.user import UserDeserializer
from app.internal.logic.entities.db.repo_settings import RepositorySettings


class RepositorySettingsDeserializer(BaseDeserializer):
    @staticmethod
    def get_from_db(record: Record) -> RepositorySettings:
        return RepositorySettings(
            id=record.get('repository_settings_id'),
            created_at=record.get('repository_settings_created_at'),
            edited_at=record.get('repository_settings_edited_at'),
            notifications=record.get('repository_settings_notifications'),
            repository_uuid=record.get('repository_settings_uuid'),
            tracked_branches=record.get('repository_settings_tracked_branches'),
            user=UserDeserializer.get_from_db(record)
        )
