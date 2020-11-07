from typing import Any, List, Tuple

import pytest
from homework2.task03.comby import combinations


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (
            [[1, 2], [3, 4], [5, 6]],
            [
                [1, 3, 5],
                [1, 3, 6],
                [1, 4, 5],
                [1, 4, 6],
                [2, 3, 5],
                [2, 3, 6],
                [2, 4, 5],
                [2, 4, 6],
            ],
        )
    ],
)
def test_combinations(value: List[List[Any]], expected_result: List[List[Any]]):
    actual_result = combinations(*value)
    assert actual_result == expected_result
