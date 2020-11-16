"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.
Write a test that check that your function works.
Test should use Mock instead of real network interactions.
You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests
>>> count_dots_on_i("https://example.com/")
59

"""
from urllib.request import urlopen


def count_dots_on_i(url: str) -> int:
    try:
        response = urlopen(url)
    except Exception as exc:
        raise ValueError(f"Unreachable {url}")

    total_sum_of_i = 0
    char = " "
    while char:
        char = response.read(1).decode("utf-8")
        total_sum_of_i += char == "i"

    return total_sum_of_i
