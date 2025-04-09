from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        unique = set()
        
        for x in nums:
            if x < k:
                return -1
            elif x > k:
                unique.add(x)
        
        return len(unique)

