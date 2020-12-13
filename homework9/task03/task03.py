"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
"""
from pathlib import Path
from typing import Callable, Iterator, Optional, TextIO, Union


def get_file_instances(path: Path, file_extension: str):
    pattern = ".".join(["**/*", file_extension])
    for file in path.glob(pattern):
        yield open(file)


def get_elements_to_count(
    file: TextIO, tokenizer: Optional[Callable]
) -> Union[TextIO, Iterator]:
    return file if tokenizer is None else map(tokenizer, file)


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    list_file = get_file_instances(dir_path, file_extension)

    amount_of_elements = 0
    for file in list_file:
        for el in get_elements_to_count(file, tokenizer):
            amount_of_elements += 1 if tokenizer is None else len(el)

    for file in list_file:
        file.close()

    return amount_of_elements
