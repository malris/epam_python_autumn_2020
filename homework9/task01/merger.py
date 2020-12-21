"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""

from heapq import merge
from pathlib import Path
from typing import Any, Generator, Iterable, Iterator, List, Tuple, Union


def get_integers_from_file(iterator: Iterator) -> Iterable[int]:
    for data in iterator:
        try:
            value = int(data)
        except ValueError:
            continue
        else:
            yield value


def get_file_integers_lists(
    file_list: Tuple[Union[Path, str], ...]
) -> Iterable[List[int]]:
    for path in file_list:
        with open(path) as file:
            yield [value for value in get_integers_from_file(file)]


def merge_sorted_files(file_list: Tuple[Union[Path, str], ...]) -> Iterator:
    list_of_files_integers = (
        int_list for int_list in get_file_integers_lists(file_list)
    )
    return merge(*list_of_files_integers)
