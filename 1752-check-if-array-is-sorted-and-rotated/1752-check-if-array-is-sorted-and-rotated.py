from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:  # Check for a decrease
                count += 1
                
            if count > 1:  # More than one decrease means it's not a valid rotated sorted array
                return False
        
        return True
