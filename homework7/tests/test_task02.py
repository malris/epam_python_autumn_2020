from typing import List

import pytest
from homework7.task02.comparison import backspace_compare, remove_service_characters


@pytest.mark.parametrize(
    ["first_str", "second_str", "expected_result"],
    [
        ["abc", "abc", True],
        ["###", "", True],
        ["##ab#c##d", "d", True],
        ["abc#de##", "a#bcde###", False],
        ["abc", "ab", False],
    ],
)
def test_backspace_compare(first_str: str, second_str: str, expected_result: bool):
    assert backspace_compare(first_str, second_str) == expected_result


@pytest.mark.parametrize(
    ["string", "expected_result"],
    [["", []], ["#", []], ["##ab#c##d", ["d"]], ["a#bcde##", ["b", "c"]]],
)
def test_remove_service_characters(string: str, expected_result: List[str]):
    assert remove_service_characters(string) == expected_result
