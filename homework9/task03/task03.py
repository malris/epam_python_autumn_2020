"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
"""
from pathlib import Path
from typing import Callable, Iterable, Optional, TextIO


def get_file_instances(path: Path, file_extension: str) -> Iterable[TextIO]:
    pattern = f"**/*.{file_extension}"
    for file in path.glob(pattern):
        with open(file) as f_it:
            yield f_it


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    list_file = get_file_instances(dir_path, file_extension)
    amount_of_elements = 0

    for file in list_file:
        elements_to_count = map(tokenizer, file) if tokenizer else file
        amount_of_elements += sum(
            len(el) if tokenizer else 1 for el in elements_to_count
        )

    return amount_of_elements
