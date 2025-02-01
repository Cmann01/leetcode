from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:  # Check if both numbers have the same parity
                return False
        return True

# Example test cases
sol = Solution()
print(sol.isArraySpecial([1]))  # True
print(sol.isArraySpecial([2, 1, 4]))  # True
print(sol.isArraySpecial([4, 3, 1, 6]))  # False
