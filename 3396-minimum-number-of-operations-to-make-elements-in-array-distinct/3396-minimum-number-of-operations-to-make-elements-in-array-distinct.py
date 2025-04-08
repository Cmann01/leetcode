from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        for ops in range(0, (n + 2) // 3 + 1):
            new_start = ops * 3
            if new_start >= n:
                # All elements removed, array is empty → distinct by default
                return ops
            subarray = nums[new_start:]
            if len(subarray) == len(set(subarray)):
                # Subarray has all distinct elements
                return ops
        return 0  # Default return (should never hit this due to constraints)
