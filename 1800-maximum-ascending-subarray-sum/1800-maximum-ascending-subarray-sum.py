from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]  # Initialize with the first element
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # Continue the ascending subarray
                current_sum += nums[i]
            else:  # Reset for a new subarray
                max_sum = max(max_sum, current_sum)
                current_sum = nums[i]
        
        return max(max_sum, current_sum)  # Ensure the last subarray is considered