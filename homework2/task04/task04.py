"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from collections import Callable, deque
from typing import Any, Sequence


def cache(func: Callable) -> Callable:
    cache_func_results = {}
    cache_order_queue = deque(maxlen=50)

    def wrapper(*args: Sequence[Any]) -> Any:
        if args not in cache_func_results:
            cache_func_results[args] = func(*args)
            cache_order_queue.append(args)
        else:
            cache_order_queue.remove(args)
            cache_order_queue.append(args)

        return cache_func_results[args]

    return wrapper
