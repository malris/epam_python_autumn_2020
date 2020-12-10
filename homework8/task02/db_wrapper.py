"""
Write a wrapper class TableData for database table,
that when initialized with database name and table acts as collection object
(implements Collection protocol).
Assume all data has unique values in 'name' column.
So, if presidents = TableData(database_name='example.sqlite', table_name='presidents'), then:

    - len(presidents) will give current amount of rows in presidents table in database
    - presidents['Yeltsin'] should return single data row for president with name Yeltsin
    - 'Yeltsin' in presidents should return if president with same name exists in table
        object implements iteration protocol. i.e. you could use it in for loops::
        for president in presidents:
            print(president['name'])
all above mentioned calls should reflect most recent data.
If data in table changed after you created collection instance, your calls should return updated data.
Avoid reading entire table into memory.
When iterating through records, start reading the first record, then go to the next one, until records are exhausted.
When writing tests, it's not always neccessary to mock database calls completely.
Use supplied example.sqlite file as database fixture file.
"""


import sqlite3
from contextlib import contextmanager
from typing import Sized


@contextmanager
def open_TableData(database_name: str, table_name: str):
    connection = sqlite3.connect(database_name)
    connection.row_factory = sqlite3.Row
    table_data = TableData(database_name, table_name, connection)
    try:
        yield table_data
    finally:
        table_data.close_connection()


class TableData(Sized):
    def __init__(self, database_name: str, table_name: str, connection: sqlite3.dbapi2):
        self.database_name = database_name
        self.table_name = table_name
        self.connection = connection

    def __len__(self) -> int:
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"SELECT COUNT(*) FROM {self.table_name}")
        except sqlite3.Error:
            amount_of_rows = 0
        else:
            amount_of_rows = cursor.fetchone()[0]
        return amount_of_rows

    def __getitem__(self, item) -> tuple:
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                f"SELECT * FROM {self.table_name} WHERE name=:name", {"name": item}
            )
        except sqlite3.Error:
            raise IndexError("name out of range")
        else:
            query_result = cursor.fetchone()
            if not query_result:
                raise IndexError("name out of range")

        return tuple(query_result)

    def __contains__(self, item: str) -> bool:
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                f"SELECT * FROM {self.table_name} WHERE name=:name", {"name": item}
            )
        except sqlite3.Error:
            contains = False
        else:
            contains = bool(cursor.fetchone())

        return contains

    def __iter__(self) -> "TableDataIter":
        return TableDataIter(self)

    def get_rows(self) -> list:
        n = self.__len__()
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"SELECT * FROM {self.table_name}")
        except sqlite3.Error:
            rows = []
        else:
            rows = [tuple(cursor.fetchone()) for _ in range(n)]

        return rows

    def close_connection(self):
        self.connection.close()


class TableDataIter:
    def __init__(self, table_data: TableData):
        self.rows = table_data.get_rows()
        self._cursor = 0

    def __iter__(self) -> "TableDataIter":
        return self

    def __next__(self) -> tuple:
        if len(self.rows) > self._cursor:
            result = self.rows[self._cursor]
            self._cursor += 1
            return result
        raise StopIteration
