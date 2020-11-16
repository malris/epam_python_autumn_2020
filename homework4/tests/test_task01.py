import os
from typing import Any

import pytest
from homework4.task01.read_file import read_magic_number


@pytest.fixture
def file_cleaner():
    open("test_file.txt", "w+").close()
    yield os.path.join(os.path.dirname(__file__), "test_file.txt")
    os.remove("test_file.txt")


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (1, True),
        (1.0, True),
        (2.5, True),
        (2.99, True),
        (-2, False),
        (0.5, False),
        (3, False),
        (3.0, False),
    ],
)
def test_magic_number_valid_values(value: float, expected_result: bool, file_cleaner):
    test_file = file_cleaner
    with open(test_file, "w") as fi:
        fi.write(f"{value}\n")
    assert read_magic_number(test_file) is expected_result


def test_file_for_magic_number_does_not_exist():
    with pytest.raises(FileNotFoundError, match="No such file or directory"):
        read_magic_number("non_existing_file.txt")


@pytest.mark.parametrize("value", ["not_a_digit"])
def test_magic_number_raises_value_error(value: Any, file_cleaner):
    test_file = file_cleaner
    with open(test_file, "w") as fi:
        fi.write(f"{value}\n")
        with pytest.raises(ValueError, match="line can't be transformed to float."):
            read_magic_number(test_file)
