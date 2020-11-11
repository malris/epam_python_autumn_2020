from typing import Any

import pytest
from homework3.task02.calculator.calc import *


@pytest.mark.parametrize(
    ["value", "expected_result"], [(15, 2358), ("bla", 1749), ("", 2121)]
)
def test_slow_calculations(value: Any, expected_result: int):
    actual_result = slow_calculate(value)
    assert actual_result == expected_result


@pytest.mark.parametrize(["expected_result"], [[1024259]])
def test_sum_of_slow_calculations(expected_result: int):
    actual_result = sum_slow_calculations()
    assert actual_result == expected_result
