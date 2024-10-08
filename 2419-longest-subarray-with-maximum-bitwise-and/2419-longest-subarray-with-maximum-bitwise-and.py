from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Step 1: Find the maximum value in the array
        max_val = max(nums)
        
        # Step 2: Find the length of the longest subarray with all elements equal to max_val
        longest = 0
        current_length = 0
        
        for num in nums:
            if num == max_val:
                current_length += 1
                longest = max(longest, current_length)
            else:
                current_length = 0
        
        return longest
