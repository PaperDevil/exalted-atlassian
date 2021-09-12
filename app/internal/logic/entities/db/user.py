from datetime import datetime
from typing import Optional

from app.internal.logic.entities.db.base import AbstractDbModel


class User(AbstractDbModel):
    def __init__(self,
                 id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None,
                 telegram_id: Optional[str] = None,
                 email: Optional[str] = None
                 ):
        super().__init__(id, created_at, edited_at)
        self.telegram_id = telegram_id
        self.email = email
