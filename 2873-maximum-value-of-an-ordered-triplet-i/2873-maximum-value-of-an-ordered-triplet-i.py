from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_val = 0
        max_i = nums[0]  # Track max nums[i] encountered so far
        max_diff = float('-inf')  # Track max (nums[i] - nums[j]) encountered so far
        
        for j in range(1, len(nums) - 1):
            max_diff = max(max_diff, max_i - nums[j])
            max_val = max(max_val, max_diff * nums[j + 1])
            max_i = max(max_i, nums[j])
            
        return max_val