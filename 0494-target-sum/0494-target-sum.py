from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)

        # If the target is not achievable, return 0
        if (total_sum - target) < 0 or (total_sum - target) % 2 != 0:
            return 0

        # Calculate the sum of the subset (s1) that needs to be positive
        s1 = (total_sum - target) // 2

        # Use a DP array to store the number of ways to form each sum
        dp = [0] * (s1 + 1)
        dp[0] = 1  # Base case: There's one way to make the sum 0

        # Iterate through the numbers in nums
        for num in nums:
            for j in range(s1, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[s1]

# Example usage
solution = Solution()
nums1 = [1, 1, 1, 1, 1]
target1 = 3
print(solution.findTargetSumWays(nums1, target1))  # Output: 5

nums2 = [1]
target2 = 1
print(solution.findTargetSumWays(nums2, target2))  # Output: 1
