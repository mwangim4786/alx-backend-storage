#!/usr/bin/env python3
"""Redis and Python exercise"""
import uuid
from typing import Callable, Union

import redis


class Cache():
    """Cache class with redis"""

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """  """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None)\
            -> Union[str, bytes, int, float]:
        """ Get data from redis and transform it to its python type """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ Transform a redis type variable to a str python type """
        variable = self._redis.get(key)
        return variable.decode("UTF-8")

    def get_int(self, key: str) -> int:
        """ Transform a redis type variable to a str python type """
        variable = self._redis.get(key)
        try:
            variable = int(variable.decode("UTF-8"))
        except Exception:
            variable = 0
        return variable
