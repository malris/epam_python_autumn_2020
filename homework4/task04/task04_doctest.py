"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.
That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions
* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, 'Робот Фортран, чисть картошку!'
"""
from typing import List


def _get_replaced_value(n: int):
    """Return 'fizz' if the number is divisible by three,
    'buzz' if the number is divisible by five,
    a real value of a number otherwise.

    >>> _get_replaced_value(1)
    '1'
    >>> _get_replaced_value(12)
    'fizz'
    >>> _get_replaced_value(25)
    'buzz'
    """
    if not n % 3:
        return "fizz"
    elif not n % 5:
        return "buzz"
    else:
        return str(n)


def fizzbuzz(n: int) -> List[str]:
    """Return n Fizzbuzz numbers.
    :param n: amount of numbers to process
    :return: list n of Fizzbuzz numbers

    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    >>> fizzbuzz('my_string')
    Traceback (most recent call last):
        ...
    ValueError: n is not a number, n: my_string
    """
    try:
        return [_get_replaced_value(val) for val in range(1, n + 1)]
    except Exception as exc:
        raise ValueError("n is not a number, n: {}".format(n))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
