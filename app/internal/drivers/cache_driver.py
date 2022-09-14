from typing import Optional, Any, Union
import json


class CacheDriver:
    """ Can be a driver for any fast key-value storage """
    __value: dict = json.load(open('database.json', 'r+'))

    @classmethod
    async def set(cls, key: Union[int, str], val: Union[list, dict]) -> None:
        cls.__value[str(key)] = val

    @classmethod
    async def get(cls, key: Union[int, str]) -> Optional[Any]:
        return cls.__value.get(str(key))

    @classmethod
    async def get_or_create(cls, key: Union[int, str], val: Union[list, dict]) -> Optional[Any]:
        if str(key) in cls.__value:
            return cls.__value.get(str(key))
        else:
            await cls.set(str(key), val)

    @classmethod
    async def update(cls, key: Union[int, str], val: Union[list, dict]) -> Optional[Any]:
        data: Union[list, dict] = await CacheDriver.get(str(key))
        if type(data) == list and type(val) == list:
            data.append(val)
        elif type(data) == dict and type(val) == dict:
            data.update(val)
        else:
            raise TypeError(f"Val must be of type {type(data)} but is {type(val)}")
        await CacheDriver.set(str(key), data)
        return data

    @classmethod
    async def get_field(cls, key: Union[int, str], field: str) -> Optional[Any]:
        data: Union[list, dict] = await CacheDriver.get(str(key))
        return data.get(field)

    @classmethod
    async def set_field(cls, key: Union[int, str], field: str, val: Any) -> None:
        data: Union[list, dict] = await CacheDriver.get(str(key))
        data[field] = val
        await CacheDriver.set(str(key), data)

    @classmethod
    def exist(cls, key: Union[int, str]) -> bool:
        return str(key) in cls.__value

    @classmethod
    def all(cls):
        return cls.__value

    @classmethod
    def dump(cls):
        json.dump(cls.__value, open('database.json', 'w+'))