from typing import List

import pytest
from sum_of_four.sum_of_four import check_sum_of_four


@pytest.mark.parametrize(
    ["a", "b", "c", "d", "expected_result"],
    [
        ([1, 2, 3], [-2, -1, -3], [3, -1, 2], [3, 0, 2], 6),
        ([1], [1], [-1], [-1], 1),
        ([0], [0], [0], [0], 1),
        ([], [], [], [], 0),
    ],
)
def test_power_of_2(a: List, b: List, c: List, d: List, expected_result: int):
    actual_result = check_sum_of_four(a, b, c, d)
    print(actual_result == expected_result)

    assert actual_result == expected_result
