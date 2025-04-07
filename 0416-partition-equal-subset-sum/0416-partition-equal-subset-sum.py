from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # If total sum is odd, we cannot partition it equally
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        n = len(nums)
        
        # dp[i] = True if subset with sum i is possible
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: 0 sum is always possible
        
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]
