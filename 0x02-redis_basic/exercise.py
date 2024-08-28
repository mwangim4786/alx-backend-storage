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
