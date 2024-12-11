from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        events = []
        
        # Step 1: Create events for the range [nums[i] - k, nums[i] + k]
        for num in nums:
            events.append((num - k, 1))  # Start of the range
            events.append((num + k + 1, -1))  # End of the range (exclusive)
        
        # Step 2: Sort events by value, breaking ties by type (-1 before 1)
        events.sort()
        
        # Step 3: Sweep line to find the maximum overlap
        active = 0
        max_beauty = 0
        for _, event in events:
            active += event
            max_beauty = max(max_beauty, active)
        
        return max_beauty
