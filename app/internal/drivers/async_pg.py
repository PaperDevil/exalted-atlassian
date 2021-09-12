from typing import Optional

from asyncpgsa import create_pool
from asyncpg.pool import Pool


class AsyncPg:
    __pool_db: Optional[Pool] = None

    @classmethod
    def get_pool_db(cls) -> Pool:
        return cls.__pool_db

    @classmethod
    async def init_db(cls, host: str, user: str, password: str, port: int, database: str,
                      min_size: Optional[int] = 10, max_size: Optional[int] = 10):
        cls.__pool_db = await create_pool(host=host, user=user, password=password, port=port, database=database,
                                          min_size=min_size, max_size=max_size)

    @classmethod
    async def close_pool_db(cls) -> None:
        await cls.__pool_db.close()
