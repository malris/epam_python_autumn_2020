"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    n = len(a)
    first_sum_chunk = {}
    second_sum_chunk = {}
    for i in range(n):
        for j in range(n):
            first_sum_chunk[a[i] + b[j]] = first_sum_chunk.get(a[i] + b[j], 0) + 1
            second_sum_chunk[c[i] + d[j]] = second_sum_chunk.get(c[i] + d[j], 0) + 1

    result = 0
    for first_sum_key, first_sum_value in first_sum_chunk.items():
        result += first_sum_value * second_sum_chunk.get(-1 * first_sum_key, 0)
    return result


# a = [1, 2, 3]
# b = [-2, -1, -3]
# c = [3, -1, 2]
# d = [3, 0, 2]
