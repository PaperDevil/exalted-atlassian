from asyncpg import Record


class BaseDeserializer:
    @staticmethod
    def get_from_db(record: Record) -> object:
        raise NotImplementedError
