from typing import Optional

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
