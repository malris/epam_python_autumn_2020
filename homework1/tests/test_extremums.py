from typing import Tuple

import pytest
from homework1.task03.extremums.minmax import find_maximum_and_minimum
from pytest_mock import mocker


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [("file_name1.txt", (-5, 4))],
)
def test_minmax(value: str, expected_result: Tuple[int, int], mocker):
    mocker.patch("extremums.minmax.read_list_of_values", return_value=[-1, 2, 3, 4, -5])
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result
