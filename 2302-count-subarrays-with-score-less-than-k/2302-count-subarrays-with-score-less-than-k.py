from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        total = 0
        left = 0
        current_sum = 0

        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum * (right - left + 1) >= k:
                current_sum -= nums[left]
                left += 1
            total += (right - left + 1)

        return total
