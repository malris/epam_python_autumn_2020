# """
# Some of the functions have a bit cumbersome behavior when we deal with
# positional and keyword arguments.
# Write a function that accept any iterable of unique values and then
# it behaves as range function:
# import string
# assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
# assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
# assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
# """
#
# import string
from typing import Any, List, Sequence


def custom_range(inp_range: Sequence[Any], *args: Sequence[Any]) -> Sequence[Any]:
    dict_accord = {}
    for i, char in enumerate(inp_range):
        dict_accord[char] = i

    len_args = len(args)
    start, stop, step = 0, len(inp_range), 1
    if len_args == 1:
        stop = dict_accord[args[0]]
    elif len_args == 2:
        start = dict_accord[args[0]]
        stop = dict_accord[args[1]]
    elif len_args == 3:
        start = dict_accord[args[0]]
        stop = dict_accord[args[1]]
        try:
            step = int(args[2])
        except ValueError:
            print("Error: step = {}, step should be integer".format(args[2]))
    result = list(inp_range[start:stop:step])
    return result
