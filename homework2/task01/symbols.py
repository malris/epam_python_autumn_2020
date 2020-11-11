"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from collections import defaultdict
from typing import Dict, List


def _form_longest_diverse_words_list(
    current_longest_diverse_words: List[str], words: List[str], length: int
) -> List[str]:
    words.extend(current_longest_diverse_words)
    words_dictionary = _form_words_dictionary(words)

    result = []
    for key in sorted(words_dictionary, reverse=True):
        if len(result) < length:
            result.extend(sorted(words_dictionary[key], key=len, reverse=True))
        else:
            break

    return result[:length]


def _form_words_dictionary(words: List[str]) -> Dict[int, List[str]]:
    d = defaultdict(list)
    for word in words:
        word_unique_sym_len = len(set(word))
        if word not in d[word_unique_sym_len]:
            d[word_unique_sym_len].append(word)
    return d


def get_longest_diverse_words(file_path: str) -> List[str]:
    longest_diverse_words = []
    punctuation_string = """!"#$%&'()*+,-./:;<=>?@[]^_`{|}~«»"""
    with open(file_path, "r", encoding="unicode-escape", errors="replace") as fi:
        for line in fi:
            line_with_lower_case = line.lower()
            line_without_punctuation = line_with_lower_case.translate(
                str.maketrans("", "", punctuation_string)
            )
            words = line_without_punctuation.rstrip("\n").split(" ")
            longest_diverse_words = _form_longest_diverse_words_list(
                longest_diverse_words, words, 10
            )
    return longest_diverse_words


def get_rarest_char(file_path: str) -> str:
    d = defaultdict(int)
    with open(file_path, "r", encoding="unicode-escape", errors="replace") as fi:
        for line in fi:
            for c in line:
                d[c] += 1
    return min(d, key=d.get) if d else ""


def count_punctuation_chars(file_path: str) -> int:
    counter = 0
    punctuation_string = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~«»"""
    with open(file_path, "r", encoding="unicode-escape", errors="replace") as fi:
        for line in fi:
            counter += sum(c in punctuation_string for c in line)
    return counter


def count_non_ascii_chars(file_path: str) -> int:
    counter = 0
    ascii_numbers = tuple(range(128))
    with open(file_path, "r", encoding="unicode-escape", errors="replace") as fi:
        for line in fi:
            counter += sum(ord(c) not in ascii_numbers for c in line)
    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    d = {}
    ascii_numbers = tuple(range(128))
    with open(file_path, "r", encoding="unicode-escape", errors="replace") as fi:
        for line in fi:
            for c in line:
                if ord(c) not in ascii_numbers:
                    d[c] = d[c] + 1 if c in d else 1
    return max(d, key=d.get) if d else ""
