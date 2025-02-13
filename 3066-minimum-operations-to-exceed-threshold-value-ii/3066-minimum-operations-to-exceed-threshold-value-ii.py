import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Step 1: Convert nums to a min-heap
        heapq.heapify(nums)
        
        operations = 0

        # Step 2: Apply operations until all elements are >= k
        while nums[0] < k:
            # Remove the two smallest elements
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            
            # Calculate the new element
            new_element = min(x, y) * 2 + max(x, y)
            
            # Add the new element back to the heap
            heapq.heappush(nums, new_element)
            
            # Increment the number of operations
            operations += 1

        return operations
