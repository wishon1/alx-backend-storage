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
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts the number of times a function is called.

    Args:
        method (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function for the decorated method.

        Args:
            self: The instance of the class.
            *args: Positional arguments passed to the method.
            **kwargs: Keyword arguments passed to the method.

        Returns:
            The return value of the decorated method.
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs and outputs of a
    function.

    Args:
        method (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function for the decorated method.

        Args:
            self: The instance of the class.
            *args: Positional arguments passed to the method.
            **kwargs: Keyword arguments passed to the method.

        Returns:
            The return value of the decorated method.
        """
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output

    return wrapper


def replay(fn: Callable):
    """
    Display the history of calls of a particular function.

    Args:
        fn (Callable): The function whose call history is to be
        displayed.
    """
    r = redis.Redis()
    function_name = fn.__qualname__
    value = r.get(function_name)
    try:
        value = int(value.decode("utf-8"))
    except Exception:
        value = 0

    print("{} was called {} times:".format(function_name, value))
    inputs = r.lrange("{}:inputs".format(function_name), 0, -1)
    outputs = r.lrange("{}:outputs".format(function_name), 0, -1)

    for input, output in zip(inputs, outputs):
        try:
            input = input.decode("utf-8")
        except Exception:
            input = ""

        try:
            output = output.decode("utf-8")
        except Exception:
            output = ""

        print("{}(*{}) -> {}".format(function_name, input, output))


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
