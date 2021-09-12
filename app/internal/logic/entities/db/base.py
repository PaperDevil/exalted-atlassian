from datetime import datetime
from typing import Optional


class AbstractDbModel(object):
    """
    Abstract class for all db classes
    """

    def __init__(self,
                 id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None) -> None:
        self.id = id
        self.created_at = created_at
        self.edited_at = edited_at

    @property
    def created_at_timestamp(self):
        if self.created_at:
            return round(self.created_at.timestamp())
        return None

    @property
    def edited_at_timestamp(self):
        if self.edited_at:
            return round(self.edited_at.timestamp())
        return None
