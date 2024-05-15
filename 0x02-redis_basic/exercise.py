#!/usr/bin/env python3
"""
Create a Cache class. In the __init__ method, store an instance of the
Redis client as a private variable named _redis (using redis.Redis()) and
flush the instance using flushdb.

Create a store method that takes a data argument and returns a string.
The method should generate a random key (e.g. using uuid), store the input
data in Redis using the random key and return the key.

Type-annotate store correctly. Remember that data can be a str, bytes,
int or float.
"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    Create a Cache class.

    In the __init__ method, store an instance of the Redis client as a
    private variable named _redis (using redis.Redis()) and flush the
    instance using flushdb.

    Create a store method that takes a data argument and returns a
    string. The method should generate a random key (e.g. using uuid),
    store the input data in Redis using the random key and return the key.

    Type-annotate store correctly. Remember that data can be a str, bytes,
    int or float.
    """

    def __init__(self):
        """Initialization of the cache class."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis using a random key.

        Args:
            data (Union[str, bytes, int, float]): The data to store in Redis.

        Returns:
            str: The generated random key used to store the data in Redis.
        """
        random_key = str(uuid.uuid4())

        # Ensure data is stored as bytes
        if isinstance(data, str):
            data = data.encode('utf-8')

        self._redis.set(random_key, data)
        return random_key

    def get(
        self,
        key: str,
        fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """
        Retrieve data from Redis based on the provided key.

        Args:
            key (str): The key string argument.
            fn (Optional[Callable]): An optional Callable argument used to
                convert the data back to the desired format.

        Returns:
            Union[str, bytes, int, float]: The retrieved data from Redis.
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        automatically parametrize Cache.get with the correct
        conversion function
        """
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """
        automatically parametrize Cache.get with the correct conversion
        function.
        """
        data = self.redis.get(key)
        try:
            data = int(value.decode("utf-8"))
        except Exception:
            data = 0
        return value
