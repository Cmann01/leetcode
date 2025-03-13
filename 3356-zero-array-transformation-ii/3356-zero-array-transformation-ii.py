from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        Q = len(queries)

        def checkWithDifferenceArrayTeq(nums: List[int], queries: List[List[int]], k: int) -> bool:
            diff = [0] * n

            # Apply difference array technique
            for i in range(k + 1):
                l, r, x = queries[i]
                diff[l] += x
                if r + 1 < n:
                    diff[r + 1] -= x

            cumSum = 0
            for i in range(n):
                cumSum += diff[i]
                if nums[i] - cumSum > 0:
                    return False
            
            return True

        if all(x == 0 for x in nums):
            return 0

        left, right, k = 0, Q - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if checkWithDifferenceArrayTeq(nums, queries, mid):
                k = mid + 1
                right = mid - 1
            else:
                left = mid + 1

        return k