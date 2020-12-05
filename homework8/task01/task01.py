"""
We have a file that works as key-value storage, each like is represented as key
and value separated by = symbol, example:

name=kek last_name=top song_name=shadilay power=9001

Values can be strings or integer numbers. If a value can be treated both
as a number and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:
storage = KeyValueStorage('path_to_file.txt') that has its keys and values
accessible as collection items and as attributes.

Example:
    - storage['name'] # will be string 'kek'
    - storage.song_name # will be 'shadilay'
    - storage.power # will be integer 9001

In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute
(for example when there's a line 1=something) ValueError should be raised.
File size is expected to be small, you are permitted to read it entirely into memory.
"""
from re import findall


class KeyValueStorage:
    def __init__(self, path_to_file: str):
        self.data_dict = {}
        self.form_data_dict(path_to_file)

    def __getattr__(self, key):
        return self.data_dict[key]

    def __getitem__(self, key):
        return self.data_dict[key]

    def form_data_dict(self, path_to_file):
        with open(path_to_file) as fi:
            self.data_dict = {
                pair[0]: pair[1]
                for line in fi.readlines()
                for key, value in findall("(\S+)=(\S+)", line)
                if (pair := self.form_item(key, value))
                and (not self.is_attribute_built_in(pair[0]))
            }

    def is_attribute_built_in(self, key):
        return key in self.data_dict

    @staticmethod
    def form_item(key, value):
        try:
            int(key)
        except ValueError:
            pass
        else:
            raise ValueError(
                f"invalid key to be assigned to an attribute: {key}={value}"
            )
        try:
            int_value = int(value)
        except ValueError:
            pair = (key, value)
        else:
            pair = (key, int_value)
        return pair
