from typing import Any, Callable, Dict, List, Sequence

import pytest
from homework3.task03.filter.filter import Filter, make_filter

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ({"name": "polly", "type": "bird"}, [sample_data[1]]),
        ({"name": "Bill", "type": "bird", "occupation": "was here"}, []),
        ({"name": "Bill", "occupation": "was here"}, [sample_data[0]]),
        ({}, []),
    ],
)
def test_filter_maker(value: Dict[Any, Any], expected_result: List[Any]):
    actual_result = make_filter(**value).apply(sample_data)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["functions", "expected_result"],
    [
        (
            (lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)),
            [2, 4, 6, 8],
        )
    ],
)
def test_filter(functions: Sequence[Callable], expected_result: List[Any]):
    filter_instance = Filter(*functions)
    actual_result = filter_instance.apply(range(10))
    assert actual_result == expected_result
