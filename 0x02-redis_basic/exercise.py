#!/usr/bin/env python3
"""Writing strings to Redis"""


import redis
from typing import Union
from uuid import uuid4


class Cache:
    """defines method, store instance"""

    def __init__(self):
        """store an instance of
        the Redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes data arg, return string"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
