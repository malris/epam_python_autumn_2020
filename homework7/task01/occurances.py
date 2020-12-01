"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
    "fifth": ("a", 1, True, {"bla": ["25", {"1": ["RED", {"RED": "bl"}]}]}),
    "sixth": {"RED", (True, (12, "RED"))},
}


def find_occurrences(tree: dict, element: Any) -> int:
    return _find_occurrences(tree, element)


def _find_occurrences(tree: Any, element: Any, n: int = 0) -> int:
    """
    Function recurrently counts all the inclusions of element in the tree.
    :param tree: contains multiple nested structures.
    :param element: value to be found.'
    :param n: accumulator
    """
    for key in tree:
        el = tree[key] if isinstance(tree, dict) else key
        if can_include_dict(el) and not isinstance(el, type(element)):
            n += _find_occurrences(el, element)
        elif element == el:
            n += 1
    return n


def can_include_dict(value: Any) -> bool:
    """
    Function checks if the value can potentially include dict.
    """
    return hasattr(value, "__iter__") and not isinstance(value, str)
