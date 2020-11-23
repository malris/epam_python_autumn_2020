from typing import Any, Sequence

import pytest
from homework5.safe_original_info.safe_original_info import custom_sum, print_result


@pytest.mark.parametrize(
    ["args", "expected_result"],
    [([[1, 2, 3], [4, 5]], [1, 2, 3, 4, 5]), ([1, 2, 3, 4], 10)],
)
def test_custom_sum(args: Sequence[Any], expected_result: Any):
    assert custom_sum(*args) == expected_result


def test_wrapped_custom_sum_original_info():
    original_func = custom_sum.__original_func
    assert custom_sum.__doc__ == original_func.__doc__
    assert custom_sum.__name__ == original_func.__name__


def test_wrapped_custom_sum_print_result(capfd):
    original_func = custom_sum.__original_func
    original_func(1, 2)
    out, err = capfd.readouterr()
    assert out == ""
    custom_sum(1, 2)
    out, err = capfd.readouterr()
    assert out == "3\n"
