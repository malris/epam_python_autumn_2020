"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if k <= 0:
        return 0
    n = len(nums)
    maximal_subarray_sum = sum(nums[:k])
    for i in range(n):
        for j in range(1, k + 1):
            subarray_sum = sum(nums[i : i + j])
            maximal_subarray_sum = max(subarray_sum, maximal_subarray_sum)

    return maximal_subarray_sum
