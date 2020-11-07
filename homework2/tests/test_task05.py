import string
from typing import Any, List

import pytest
from homework2.task05.task05 import custom_range


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([string.ascii_lowercase, "g"], ["a", "b", "c", "d", "e", "f"]),
        (
            [string.ascii_lowercase, "g", "p"],
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        ([string.ascii_lowercase, "p", "g", -2], ["p", "n", "l", "j", "h"]),
        (
            [string.ascii_lowercase],
            [
                "a",
                "b",
                "c",
                "d",
                "e",
                "f",
                "g",
                "h",
                "i",
                "j",
                "k",
                "l",
                "m",
                "n",
                "o",
                "p",
                "q",
                "r",
                "s",
                "t",
                "u",
                "v",
                "w",
                "x",
                "y",
                "z",
            ],
        ),
    ],
)
def test_custom_range(value: List[List[Any]], expected_result: List[List[Any]]):
    actual_result = custom_range(*value)
    assert actual_result == expected_result
