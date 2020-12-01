"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""
from re import sub
from typing import List


def backspace_compare(first: str, second: str):
    return remove_service_characters(first) == remove_service_characters(second)


def remove_service_characters(string: str) -> List[str]:
    listed_string = []
    for char in string:
        if char != "#":
            listed_string.append(char)
        elif listed_string:
            listed_string.pop()

    return listed_string
