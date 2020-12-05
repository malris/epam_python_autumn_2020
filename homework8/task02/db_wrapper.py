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


import os
import sqlite3
from functools import wraps
from typing import Sized


def connected(f):
    @wraps(f)
    def wrapped(*args):
        self = args[0]
        with sqlite3.connect(self.database_name) as connection:
            connection.row_factory = sqlite3.Row
            self.cursor = connection.cursor()
            res = f(*args)
        return res

    return wrapped


class TableData(Sized):
    def __init__(self, database_name: str, table_name: str):
        self.database_name = database_name
        self.table_name = table_name

        self.cursor = None

    @connected
    def __len__(self) -> int:
        try:
            self.cursor.execute(f"SELECT COUNT(*) FROM {self.table_name}")
        except sqlite3.Error:
            amount_of_rows = 0
        else:
            amount_of_rows = self.cursor.fetchone()[0]
        return amount_of_rows

    @connected
    def __getitem__(self, item):
        try:
            self.cursor.execute(
                f"SELECT * FROM {self.table_name} WHERE name=:name", {"name": item}
            )
        except sqlite3.Error:
            raise IndexError("name out of range")

        query_result = self.cursor.fetchone()
        if not query_result:
            raise IndexError("name out of range")

        return tuple(query_result)

    @connected
    def __contains__(self, item):
        try:
            self.cursor.execute(
                f"SELECT * FROM {self.table_name} WHERE name=:name", {"name": item}
            )
        except sqlite3.Error:
            contains = False
        else:
            contains = bool(self.cursor.fetchone())

        return contains

    @connected
    def __iter__(self):
        n = self.__len__()
        try:
            self.cursor.execute(f"SELECT * FROM {self.table_name}")
        except sqlite3.Error:
            iterable_db = iter([])
        else:
            iterable_db = (tuple(self.cursor.fetchone()) for _ in range(n))

        return iterable_db
