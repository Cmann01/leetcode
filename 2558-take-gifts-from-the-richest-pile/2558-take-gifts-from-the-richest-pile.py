import heapq
import math
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Convert the list into a max-heap by pushing negative values
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            # Get the pile with the maximum gifts
            max_gifts = -heapq.heappop(max_heap)
            # Leave behind floor(sqrt(max_gifts))
            remaining_gifts = math.floor(math.sqrt(max_gifts))
            # Push the remaining gifts back into the heap
            heapq.heappush(max_heap, -remaining_gifts)
        
        # Sum the remaining gifts in all piles
        return -sum(max_heap)
