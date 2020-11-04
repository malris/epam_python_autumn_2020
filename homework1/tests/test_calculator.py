import pytest
from calculator.calc import check_power_of_2


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [(65536, True), (12, False), (-1, False), (0, False), (1, True)],
)
def test_power_of_2(value: int, expected_result: bool):
    actual_result = check_power_of_2(value)
    print(actual_result == expected_result)

    assert actual_result == expected_result
