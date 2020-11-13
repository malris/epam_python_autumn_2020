from typing import Any, Callable, Collection, List


def cache(times: int = 1) -> Callable:
    """A decorator for caching of functions return values.

    :param times: the number of cached returns of the function.
    """

    def wrapper(func: Callable) -> Callable:
        cache_func_results = {}

        def wrapped(*args: Collection[Any]) -> Any:
            args_in_cache = bool(args in cache_func_results)
            if (not args_in_cache) or (
                args_in_cache and cache_func_results[args][1] >= times
            ):
                cache_func_results[args] = [func(*args), 0]
            else:
                cache_func_results[args][1] += 1
            return cache_func_results[args][0]

        return wrapped

    return wrapper


@cache(times=2)
def power_func(a: int, b: int) -> List[int]:
    return [a, b]


@cache(times=2)
def inp_func() -> str:
    return input("? ")
