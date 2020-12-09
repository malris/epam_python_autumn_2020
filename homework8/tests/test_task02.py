import os

import pytest
from homework8.task02.db_wrapper import open_TableData


def get_db_name():
    path_to_db = os.path.join(os.path.dirname(__file__), "test_staff/example.sqlite")
    return path_to_db


@pytest.mark.parametrize(
    ["table_name", "expected_result"],
    [["presidents", 3], ["books", 3], ["non_existed_table", 0]],
)
def test_get_table_length(table_name: str, expected_result: int):
    with open_TableData(get_db_name(), table_name) as table:
        assert len(table) == expected_result


@pytest.mark.parametrize(
    ["table_name", "item", "expected_result"],
    [
        ["presidents", "Yeltsin", ("Yeltsin", 999, "Russia")],
        ["books", "Farenheit 451", ("Farenheit 451", "Bradbury")],
    ],
)
def test_getitem_of_table(table_name: str, item: str, expected_result: tuple):
    with open_TableData(get_db_name(), table_name) as table:
        assert table[item] == expected_result


@pytest.mark.parametrize(
    ["table_name", "item"],
    [["non_existed_table", "Yeltsin"], ["books", "non_existed_book"]],
)
def test_getitem_of_table_raises_index_error(table_name: str, item: str):
    with open_TableData(get_db_name(), table_name) as table:
        with pytest.raises(IndexError, match="name out of range"):
            table[item]


@pytest.mark.parametrize(
    ["table_name", "item", "expected_result"],
    [
        ["presidents", "Yeltsin", True],
        ["non_existed_table", "Bla", False],
        ["presidents", "non_existed_item", False],
    ],
)
def test_table_contains_item(table_name: str, item: str, expected_result: bool):
    with open_TableData(get_db_name(), table_name) as table:
        assert (item in table) is expected_result


def test_table_is_iterable():
    with open_TableData(get_db_name(), "presidents") as presidents:
        actual_result = [president[0] for president in presidents]
        assert actual_result == ["Yeltsin", "Trump", "Big Man Tyrone"]
