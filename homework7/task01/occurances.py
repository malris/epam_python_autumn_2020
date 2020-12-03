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
    "sixth": {12: "RED", 13: (True, (12, {1: "RED", 2: "BLUE"}))},
}

dd = {"fff": (1, {1: 2})}


def find_occurrences(tree: dict, element: Any) -> int:
    """
    Function recurrently counts all the inclusions of element in the tree.
    :param tree: contains multiple nested structures.
    :param element: value to be found.'
    """
    n = 0
    for key in tree:
        value = tree[key] if isinstance(tree, dict) else key
        if can_include_elements(value) and not isinstance(value, type(element)):
            n += find_occurrences(value, element)
        elif element == value:
            n += 1
    return n


def can_include_elements(value: Any) -> bool:
    """
    Function checks if the value can include several elements .
    """
    return isinstance(value, (list, tuple, set, dict))
