import heapq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # Convert nums into a max-heap (simulated using negatives)
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        score = 0
        
        for _ in range(k):
            # Get the largest element
            largest = -heapq.heappop(max_heap)
            score += largest
            # Replace it with ceil(largest / 3)
            heapq.heappush(max_heap, -math.ceil(largest / 3))
        
        return score
