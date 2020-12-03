from typing import Any

import pytest
from homework7.task01.occurances import can_include_elements, find_occurrences


@pytest.mark.parametrize(
    ["tree", "element", "expected_result"],
    [
        [{"first": [1, 2, {"nested": 1}]}, 1, 2],
        [{12: (False, "str", {1, 2, True})}, True, 1],
        [{"first": "RED", "second": ([1, True], {1: "RED"})}, "RED", 2],
        [{"first": 1, 12: [(1, 2), True], "third": {13: (1, 2)}}, (1, 2), 2],
    ],
)
def test_different_element_types(tree: dict, element: Any, expected_result: int):
    assert find_occurrences(tree, element) == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (1, False),
        (True, False),
        ("str", False),
        ([1, 2, "3"], True),
        ({1: 2}, True),
        ((1, 2), True),
    ],
)
def test_value_can_include_dict(value: Any, expected_result: bool):
    assert can_include_elements(value) is expected_result
