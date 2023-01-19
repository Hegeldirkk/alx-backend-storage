#!/usr/bin/env python3
"""Writing strings to Redis"""


import redis
from typing import Union, Callable
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

    def get(self, key: str, fn: Callable= None):
        """convert data for desired format"""
        call = self._redis.get(key)
        if fn is not None:
            return fn(call)
        return call

    def get_str(self, key: str) -> str:
        """Cache.get with the correct conversion"""
        getstr = self._redis.get(key)
        return getstr.decode('UTF-8')

    def get_int(self, key: str) -> int:
        """Cache.get with the correct conversion"""
        getint = self._redis.get(key)
        try:
            getint = int(getint.decode('UTF-8'))
        except Exception:
            getint = 0
        return getint
