from typing import Optional

from asyncpg import UniqueViolationError
from sqlalchemy import select, func, and_

from app.internal.logic.dao.base import BaseDao
from app.internal.logic.deserializers.user import UserDeserializer
from app.internal.logic.entities.db.user import User
from app.schema.meta import user_table


class UserDao(BaseDao):
    deserializer = UserDeserializer
    default_rows = [
        user_table.c.id.label('user_id'),
        user_table.c.created_at.label('user_created_at'),
        user_table.c.edited_at.label('user_updated_at'),
        user_table.c.telegram_id.label('user_telegram_id'),
        user_table.c.email.label('user_email')
    ]

    async def add(self, user: User) -> Optional[User]:
        query = user_table.insert(values={
            'telegram_id': user.telegram_id
        }).returning(user_table.c.id)

        async with self.connection as conn:
            try:
                user_id = await conn.fetchval(query)
            except UniqueViolationError as exc:
                raise

        user.id = user_id
        return user

    async def get_by_id(self, id: int) -> Optional[User]:
        query = select(self.default_rows).select_from(user_table).where(
            user_table.c.id == id
        )
        return await self.get_object_by_field(query)

    async def get_by_telegram_id(self, telegram_id: str) -> Optional[User]:
        query = select(self.default_rows).select_from(user_table).where(
            user_table.c.telegram_id == telegram_id
        )
        return await self.get_object_by_field(query)
