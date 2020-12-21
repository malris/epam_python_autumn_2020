from pathlib import Path
from re import findall
from typing import Callable

import pytest
from homework9.task03.task03 import universal_file_counter


def get_root_dir():
    return Path(__file__).parent.parent.parent


@pytest.mark.parametrize(
    ["dir", "extension", "expected_result"],
    [
        ["homework1/task02", "py", 19],
        ["homework1", "txt", 12],
        ["homework1", "doc", 0],
    ],
)
def test_universal_file_counter_without_tokenizer(
    dir: str, extension: str, expected_result: int
):
    p = get_root_dir() / dir
    assert universal_file_counter(p, extension) == expected_result


@pytest.mark.parametrize(
    ["dir", "extension", "tokenizer", "expected_result"],
    [
        ["homework1/task02", "py", str.split, 91],
        ["homework1/task02", "py", lambda line: findall("(\S+) = (\S+)", line), 2],
    ],
)
def test_universal_file_counter_with_tokenizer(
    dir: str, extension: str, tokenizer: Callable, expected_result: int
):
    p = get_root_dir() / dir
    assert universal_file_counter(p, extension, tokenizer) == expected_result
