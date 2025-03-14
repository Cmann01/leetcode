from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0  # Not enough candies for each child to get at least one

        low, high = 1, max(candies)
        result = 0
        
        while low <= high:
            mid = (low + high) // 2
            count = sum(c // mid for c in candies)
            
            if count >= k:
                result = mid  # Mid is a valid answer, try for a larger one
                low = mid + 1
            else:
                high = mid - 1
        
        return result
