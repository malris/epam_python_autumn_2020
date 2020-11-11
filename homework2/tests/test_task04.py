from typing import Any, Callable, Sequence

import pytest
from homework2.task04.task04 import cache


@pytest.mark.parametrize(
    ["function", "args"],
    [
        (lambda a, b: (a ** b) ** 2, (20, 15)),
        (lambda a, b: (a ** b) ** 2, (100, 200)),
        (lambda a, b: (a ** b) ** 2, (0, 0)),
        (lambda a, b: (a ** b) ** 2, (-58, 25)),
    ],
)
def test_cache(function: Callable, args: Sequence[Any]):
    cache_func = cache(function)
    actual_result_1 = cache_func(*args)
    actual_result_2 = cache_func(*args)
    actual_result_3 = cache_func(*args)
    assert actual_result_1 is actual_result_2 is actual_result_3
