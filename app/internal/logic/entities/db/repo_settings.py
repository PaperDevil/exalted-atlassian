from datetime import datetime
from typing import Optional

from app.internal.logic.entities.db.base import AbstractDbModel
from app.internal.logic.entities.db.user import User


class RepositorySettings(AbstractDbModel):
    def __init__(self,
                 id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None,
                 notifications: Optional[bool] = None,
                 repository_uuid: Optional[str] = None,
                 tracked_branches: Optional[list] = None,
                 user: Optional[User] = User()
                 ):
        super().__init__(id, created_at, edited_at)
        self.notifications = notifications
        self.repository_uuid = repository_uuid
        self.tracked_branches = tracked_branches
        self.user = user
