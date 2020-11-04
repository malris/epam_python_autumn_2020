"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""
from typing import List, Tuple


def read_list_of_values(file_name: str) -> List[int]:
    list_of_values = []
    with open(file_name, "r") as fi:
        for line in fi:
            list_of_values.append(int(line))
    return list_of_values


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    list_of_values = read_list_of_values(file_name)
    return min(list_of_values), max(list_of_values)
