from contextlib import asynccontextmanager

from typing import List, Optional

from asyncpg import Connection
from asyncpg.pool import Pool

from app.internal.drivers.async_pg import AsyncPg
from app.internal.logic.deserializers.base import BaseDeserializer


class BaseDao:

    deserializer: BaseDeserializer
    default_rows: list

    def __init__(self, conn: Optional[Connection] = None) -> None:
        self.pool: Pool = AsyncPg.get_pool_db()
        self._conn: Connection = conn

    @property
    @asynccontextmanager
    async def connection(self):
        if self._conn:
            yield self._conn
        else:
            self._conn = await self.pool.acquire()
            try:
                yield self._conn
            except Exception:
                raise
            finally:
                await self.pool.release(self._conn)

    async def get_by_id(self, id: int) -> object:
        raise NotImplementedError

    async def add(self, obj: object) -> object:
        raise NotImplementedError

    async def add_many(self, objs: List[object]) -> None:
        raise NotImplementedError

    async def remove(self, obj: object) -> None:
        raise NotImplementedError

    async def remove_by_id(self, id: int) -> object:
        raise NotImplementedError

    async def get_all(self, limit, offset) -> List[object]:
        raise NotImplementedError

    async def update(self, id, obj: object) -> object:
        raise NotImplementedError

    async def get_object_by_field(self, query) -> Optional[object]:
        async with self.connection as conn:
            row = await conn.fetchrow(query)

        if not row:
            return None

        return self.deserializer.get_from_db(row)
