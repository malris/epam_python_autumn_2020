from typing import List

import pytest
from homework9.task01.merger import get_numbers, merge_sorted_files


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        [[], []],
        [["not_a_number"], []],
        [["1", "2", "3"], [1, 2, 3]],
        [["not_a_number", "1", "2"], [1, 2]],
        [["1", "not_a_number", "2"], [1, 2]],
        [["1", "2", "not_a_number"], [1, 2]],
        [["1", "2", "7,2", "15.52"], [1, 2]],
    ],
)
def test_get_numbers(data: List[str], expected_result: List[int]):
    assert list(get_numbers(data)) == expected_result


def test_merge_sorted_files():
    result_list = list(merge_sorted_files(["test_staff/f1.txt", "test_staff/f2.txt"]))
    assert result_list == [1, 2, 3, 4, 5, 6, 12]
