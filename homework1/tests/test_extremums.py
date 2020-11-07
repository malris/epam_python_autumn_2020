from typing import Tuple

import pytest
from homework1.task03.extremums.minmax import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("test_staff/list_of_values.txt", (-8, 5)),
        ("test_staff/list_of_values1.txt", (1, 2)),
        ("test_staff/list_of_values2.txt", (None, None)),
    ],
)
def test_minmax(value: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result
