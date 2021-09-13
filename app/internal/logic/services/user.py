from typing import Optional

from app.external.logic.services import BitbucketOAuth2Service
from app.internal.drivers.cache_driver import CacheDriver
from app.internal.logic.dao.user import UserDao
from app.internal.logic.entities.db.user import User
from app.internal.logic.services.base import BaseService


class UserService(BaseService):
    @staticmethod
    async def create_user(telegram_id: str) -> Optional[User]:
        exist_user: Optional[User] = await UserDao().get_by_telegram_id(telegram_id)
        if exist_user:
            user = exist_user
        else:
            user: Optional[User] = await UserDao().add(User(telegram_id=telegram_id))

        return user

    @staticmethod
    async def get_user_by_id(user_id: int) -> Optional[User]:
        user: User = await UserDao().get_by_id(user_id)
        return user

    @staticmethod
    async def auth_bitbucket(user_id: int, state: str, code: str) -> None:
        access_token = await BitbucketOAuth2Service.get_access_token(state, code)
        user_cache = await CacheDriver.get(user_id)
        if not user_cache:
            await CacheDriver.set(user_id, {})
        await CacheDriver.set_field(user_id, 'access_token', access_token)
