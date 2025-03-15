from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def canRobWithCapability(capability: int) -> bool:
            count, i = 0, 0
            while i < len(nums):
                if nums[i] <= capability:
                    count += 1
                    i += 1  # Skip adjacent house
                i += 1  # Move to the next house
            return count >= k

        low, high = min(nums), max(nums)
        while low < high:
            mid = (low + high) // 2
            if canRobWithCapability(mid):
                high = mid  # Try for a lower capability
            else:
                low = mid + 1  # Increase capability
        
        return low
