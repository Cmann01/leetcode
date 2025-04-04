from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Step 1: Apply the operations
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        # Step 2: Shift all zeros to the end
        non_zero = [num for num in nums if num != 0]
        zero_count = n - len(non_zero)
        
        return non_zero + [0] * zero_count
