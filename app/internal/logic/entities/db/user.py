from datetime import datetime
from typing import Optional

from app.external.drivers.bitbucket import BitbucketDriver
from app.internal.drivers.cache_driver import CacheDriver
from app.internal.logic.entities.common.user import BitbucketUser
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

    @property
    async def access_token(self) -> str:
        tokens = await CacheDriver.get_field(self.id, 'access_token')
        return tokens['access_token']

    @property
    async def account(self) -> BitbucketUser:
        return await BitbucketDriver(
            await self.access_token
        ).get_current_user()

    async def get_session(self) -> Optional[dict]:
        return await CacheDriver.get_or_create(f'{self.id}', {})

    async def update_session(self, val):
        await CacheDriver.update(f'{self.id}', val)
