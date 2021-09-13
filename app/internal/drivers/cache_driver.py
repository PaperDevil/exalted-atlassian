from typing import Optional, Any, Union


class CacheDriver:
    """ Can be a driver for any fast key-value storage """
    __value: dict = {}

    @classmethod
    async def set(cls, key: Union[int, str], val: Union[list, dict]) -> None:
        cls.__value[key] = val

    @classmethod
    async def get(cls, key: Union[int, str]) -> Optional[Any]:
        return cls.__value.get(key)

    @classmethod
    async def update(cls, key: Union[int, str], val: Union[list, dict]) -> Optional[Any]:
        data: Union[list, dict] = await CacheDriver.get(key)
        if type(data) == list and type(val) == list:
            data.append(val)
        elif type(data) == dict and type(val) == dict:
            data.update(val)
        else:
            raise TypeError(f"Val must be of type {type(data)} but is {type(val)}")
        await CacheDriver.set(key, data)
        return data

    @classmethod
    async def get_field(cls, key: Union[int, str], field: str) -> Optional[Any]:
        data: Union[list, dict] = await CacheDriver.get(key)
        return data.get(field)

    @classmethod
    async def set_field(cls, key: Union[int, str], field: str, val: Any) -> None:
        data: Union[list, dict] = await CacheDriver.get(key)
        data[field] = val
        await CacheDriver.set(key, data)

    @classmethod
    def exist(cls, key: Union[int, str]) -> bool:
        return key in cls.__value
