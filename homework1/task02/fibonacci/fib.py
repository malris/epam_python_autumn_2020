from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) < 3:
        return False
    i = 0
    while i < len(data) - 2:
        a, b, c = data[i], data[i + 1], data[i + 2]
        if a + b != c:
            return False
        i += 1
    return True
