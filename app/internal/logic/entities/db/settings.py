from datetime import datetime
from typing import Optional

from app.internal.logic.entities.db.base import AbstractDbModel
from app.internal.logic.entities.db.user import User


class Settings(AbstractDbModel):
    def __init__(self,
                 id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None,
                 notifications: Optional[bool] = None,
                 user: Optional[User] = User()
                 ):
        super().__init__(id, created_at, edited_at)
        self.notifications = notifications
        self.user = user
