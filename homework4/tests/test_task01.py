import os
from typing import Any

import pytest
from homework4.task01.read_file import read_magic_number


@pytest.fixture
def file_cleaner():
    test_file = open("test_file.txt", "w")
    yield
    test_file.close()
    os.remove("test_file.txt")


@pytest.mark.usefixtures("file_cleaner")
@pytest.mark.parametrize("value", [1, 1.0, 2.5, 2.99])
def test_magic_number_is_true(value: float):
    with open("test_file.txt", "w") as fi:
        fi.write("{:f}\n".format(value))
    path_to_file = os.path.join(os.path.dirname(__file__), "test_file.txt")
    assert read_magic_number(path_to_file) is True


@pytest.mark.usefixtures("file_cleaner")
@pytest.mark.parametrize("value", [-2, 0.5, 3, 3.0])
def test_magic_number_is_false(value: float):
    with open("test_file.txt", "w") as fi:
        fi.write("{:f}\n".format(value))
    path_to_file = os.path.join(os.path.dirname(__file__), "test_file.txt")
    assert read_magic_number(path_to_file) is False


def test_file_for_magic_number_does_not_exist():
    with pytest.raises(FileNotFoundError, match="No such file or directory"):
        read_magic_number("non_existing_file.txt")


@pytest.mark.usefixtures("file_cleaner")
@pytest.mark.parametrize("value", ["not_a_digit"])
def test_magic_number_raises_value_error(value: Any):
    with open("test_file.txt", "w") as fi:
        fi.write("{}\n".format(value))
        path_to_file = os.path.join(os.path.dirname(__file__), "test_file.txt")
        with pytest.raises(ValueError, match="line can't be transformed to float."):
            read_magic_number(path_to_file)
