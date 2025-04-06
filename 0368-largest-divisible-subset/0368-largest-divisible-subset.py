from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()  # Step 1: Sort the numbers
        n = len(nums)
        dp = [1] * n         # dp[i] will store the size of the largest subset ending with nums[i]
        prev = [-1] * n      # prev[i] stores the index of the previous element in the subset
        max_idx = 0          # Index of the last element in the largest subset

        # Step 2: Fill DP table
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > dp[max_idx]:
                max_idx = i

        # Step 3: Reconstruct the subset
        result = []
        while max_idx != -1:
            result.append(nums[max_idx])
            max_idx = prev[max_idx]

        return result[::-1]  # Return in increasing order
