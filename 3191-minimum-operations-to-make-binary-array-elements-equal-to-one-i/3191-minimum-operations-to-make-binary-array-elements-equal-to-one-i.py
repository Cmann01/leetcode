from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ops = 0
        
        for i in range(n - 2):
            if nums[i] == 0:
                # Flip the next 3 elements
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ops += 1
        
        # Check if the array is fully converted to 1s
        return ops if all(num == 1 for num in nums) else -1
