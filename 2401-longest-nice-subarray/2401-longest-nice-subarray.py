from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        max_length = 0
        bitwise_and = 0
        
        for right in range(len(nums)):
            while (bitwise_and & nums[right]) != 0:
                bitwise_and ^= nums[left]
                left += 1
            
            bitwise_and |= nums[right]
            max_length = max(max_length, right - left + 1)
        
        return max_length