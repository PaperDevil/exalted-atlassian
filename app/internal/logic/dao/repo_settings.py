from app.internal.logic.dao.base import BaseDao
from app.internal.logic.deserializers.repo_settings import RepositorySettingsDeserializer
from app.schema.meta import repository_settings_table


class RepositorySettingsDao(BaseDao):
    deserializer = RepositorySettingsDeserializer
    default_rows = [
        repository_settings_table.c.id.label('repository_settings_id'),
        repository_settings_table.c.created_at.label('repository_settings_created_at'),
        repository_settings_table.c.edited_at.label('repository_settings_edited_at'),
        repository_settings_table.c.notifications.label('repository_settings_notifications'),
        repository_settings_table.c.repository_uuid.label('repository_settings_uuid'),
        repository_settings_table.c.tracked_branches.label('repository_settings_tracked_branches'),
        repository_settings_table.c.user_id.label('user_id')
    ]
