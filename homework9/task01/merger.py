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
from typing import Any, Generator, Iterator, Tuple, Union


def get_numbers(iterator: Iterator) -> Generator[int, Any, None]:
    for data in iterator:
        try:
            value = int(data)
        except ValueError:
            continue
        else:
            yield value


def get_file_iterators(
    file_list: Tuple[Union[Path, str], ...]
) -> Generator[Generator[int, Any, None], Any, None]:
    for file in map(open, file_list):
        yield (value for value in get_numbers(file))


def merge_sorted_files(file_list: Tuple[Union[Path, str], ...]) -> Iterator:
    file_iterators = (it for it in get_file_iterators(file_list))
    return merge(*file_iterators)
