from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        min_pos = max_pos = bad_pos = -1
        
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                bad_pos = i  # mark invalid position
            if num == minK:
                min_pos = i  # update last seen position of minK
            if num == maxK:
                max_pos = i  # update last seen position of maxK
            
            res += max(0, min(min_pos, max_pos) - bad_pos)
        
        return res
