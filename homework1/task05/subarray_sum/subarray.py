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
