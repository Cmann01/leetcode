from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        count = 0
        
        # Extend the array circularly for k elements to handle wrap-around
        extended_colors = colors + colors[:k-1]
        
        # Check all k-length contiguous subarrays in the original list
        for i in range(n):
            is_alternating = True
            for j in range(i, i + k - 1):
                if extended_colors[j] == extended_colors[j + 1]:
                    is_alternating = False
                    break
            if is_alternating:
                count += 1
                
        return count
