import os

import pytest
from homework8.task02.db_wrapper import TableData


def get_table_instance(table_name):
    path_to_db = os.path.join(os.path.dirname(__file__), "test_staff/example.sqlite")
    table = TableData(path_to_db, table_name)
    return table


@pytest.mark.parametrize(
    ["table_name", "expected_result"],
    [["presidents", 3], ["books", 3], ["non_existed_table", 0]],
)
def test_get_table_length(table_name: str, expected_result: int):
    table = get_table_instance(table_name)
    assert len(table) == expected_result


@pytest.mark.parametrize(
    ["table_name", "item", "expected_result"],
    [
        ["presidents", "Yeltsin", ("Yeltsin", 999, "Russia")],
        ["books", "Farenheit 451", ("Farenheit 451", "Bradbury")],
    ],
)
def test_getitem_of_table(table_name: str, item: str, expected_result: tuple):
    table = get_table_instance(table_name)
    assert table[item] == expected_result


@pytest.mark.parametrize(
    ["table_name", "item"],
    [["non_existed_table", "Yeltsin"], ["books", "non_existed_book"]],
)
def test_getitem_of_table_raises_index_error(table_name: str, item: str):
    table = get_table_instance(table_name)
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
    table = get_table_instance(table_name)
    assert (item in table) is expected_result


def test_table_is_iterable():
    presidents = get_table_instance("presidents")
    actual_result = [president[0] for president in presidents]
    assert actual_result == ["Yeltsin", "Trump", "Big Man Tyrone"]
