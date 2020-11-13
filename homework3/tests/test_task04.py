import pytest
from homework3.task04.arm.armstrong import is_armstrong


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [(-9, False), (0, True), (9, True), (10, False), (407, True), (None, False)],
)
def test_is_armstrong(value: int, expected_result: bool):
    actual_result = is_armstrong(value)
    assert actual_result == expected_result
