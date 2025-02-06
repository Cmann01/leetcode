from collections import defaultdict
from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)
        count = 0
        
        # Iterate through all pairs and store product frequencies
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                product_count[product] += 1
        
        # Calculate the number of valid tuples
        for val in product_count.values():
            if val > 1:
                count += (val * (val - 1)) // 2 * 8  # (Combinations * 8 permutations)
                
        return count
