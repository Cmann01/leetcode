from collections import defaultdict
from typing import List

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1  # Base case: empty prefix
        count = 0
        current = 0
        
        for num in nums:
            if num % modulo == k:
                current += 1
            
            # We want (current - prev) % modulo == k
            # => prev % modulo == (current - k + modulo) % modulo
            target = (current - k + modulo) % modulo
            
            count += prefix_count[target]
            prefix_count[current % modulo] += 1
        
        return count
