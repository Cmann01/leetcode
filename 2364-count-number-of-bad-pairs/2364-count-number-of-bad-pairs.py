from collections import defaultdict
from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total_pairs = n * (n - 1) // 2  # Total number of pairs (i, j) where i < j
        count_map = defaultdict(int)
        good_pairs = 0
        
        for j in range(n):
            diff = nums[j] - j  # Transforming the condition to (nums[j] - j)
            good_pairs += count_map[diff]  # Count pairs that satisfy the condition
            count_map[diff] += 1  # Update the count of this difference
        
        return total_pairs - good_pairs  # Bad pairs = Total pairs - Good pairs
