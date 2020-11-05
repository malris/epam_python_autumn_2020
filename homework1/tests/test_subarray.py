from typing import List

import pytest
from homework1.task05.subarray_sum.subarray import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["list_of_nums", "k", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([1, 3, -1, -3, 5, 3, 6, 7], -5, 0),
        ([1, 3, -1, -3, 5, 3, 6, 7], 0, 0),
        ([1, 3, -1, -3, 5, 3, 6, 7], 1, 7),
        ([1, 3, -1, -3, 5, 3, 6, 7], 6, 21),
        ([1, 4, -1, -3, 5, 3, 6, 7], 8, 22),
        ([1, 3, -1, -3, 5, 3, 6, 7], 10, 21),
    ],
)
def test_max_subarr(list_of_nums: List[int], k: int, expected_result: int):
    actual_result = find_maximal_subarray_sum(list_of_nums, k)

    assert actual_result == expected_result
