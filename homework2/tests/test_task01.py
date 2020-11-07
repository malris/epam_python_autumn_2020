import homework2.task1.symbols
import pytest


@pytest.mark.parametrize(
    ["cur_list", "words", "length", "expected_result"],
    [
        (
            ["abc", "ab"],
            ["abcddd", "abccccccc", "abcde"],
            3,
            ["abcde", "abcddd", "abccccccc"],
        ),
        (
            [],
            ["abcddd", "abccccccc", "abcde", "abcdeeeeee"],
            3,
            ["abcdeeeeee", "abcde", "abcddd"],
        ),
        (
            ["abcddd", "abccccccc", "abcde", "abcdeeeeee"],
            [],
            3,
            ["abcdeeeeee", "abcde", "abcddd"],
        ),
    ],
)
def test_form_longest_diverse_words_list(
    cur_list: list[str], words: list[str], length: int, expected_result: list[str]
):
    actual_result = homework2.task1.symbols._form_longest_diverse_words_list(
        cur_list, words, length
    )
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (
            ["abcddd", "abccccccc", "abcde"],
            {5: ["abcde"], 4: ["abcddd"], 3: ["abccccccc"]},
        ),
        (
            [
                "abcddd",
                "abccccccc",
                "abcde",
                "abcdeeeeee",
                "abcdeeeeee",
                "abcde",
                "abcddd",
            ],
            {5: ["abcde", "abcdeeeeee"], 4: ["abcddd"], 3: ["abccccccc"]},
        ),
    ],
)
def test_form_words_dictionary(value: list[str], expected_result: dict[int, list[int]]):
    actual_result = homework2.task1.symbols._form_words_dictionary(value)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (
            "test_staff/data.txt",
            [
                "unmißverständliche",
                "werkstättenlandschaft",
                "kollektivschuldiger",
                "bevölkerungsabschub",
                "politischstrategischen",
                "résistancebewegungen",
                "millionenbevölkerung",
                "selbstverständlich",
                "friedensabstimmung",
                "kirchenverfolgung",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(value: str, expected_result: str):
    actual_result = homework2.task1.symbols.get_longest_diverse_words(value)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [("test_staff/my_test_data.txt", "a"), ("test_staff/data.txt", "›")],  # \u203a
)
def test_get_rarest_char(value: str, expected_result: str):
    actual_result = homework2.task1.symbols.get_rarest_char(value)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("test_staff/my_test_data.txt", 29),
        ("test_staff/data.txt", 5391),
    ],
)
def test_count_punctuation_chars(value: str, expected_result: int):
    actual_result = homework2.task1.symbols.count_punctuation_chars(value)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("test_staff/my_test_data.txt", 0),
        ("test_staff/data.txt", 2972),
    ],
)
def test_count_non_ascii_chars(value: str, expected_result: int):
    actual_result = homework2.task1.symbols.count_non_ascii_chars(value)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("test_staff/my_test_data.txt", ""),
        ("test_staff/data.txt", "ä"),
    ],
)
def test_get_most_common_non_ascii_char(value: str, expected_result: int):
    actual_result = homework2.task1.symbols.get_most_common_non_ascii_char(value)
    assert actual_result == expected_result
