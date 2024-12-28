from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # Compute the sum of every k-length subarray
        sums = [0] * (n - k + 1)
        current_sum = sum(nums[:k])
        sums[0] = current_sum
        for i in range(1, len(sums)):
            current_sum += nums[i + k - 1] - nums[i - 1]
            sums[i] = current_sum
        
        # Arrays to store the best index for left and right intervals
        left = [0] * len(sums)
        right = [0] * len(sums)
        
        # Fill the left array
        max_index = 0
        for i in range(len(sums)):
            if sums[i] > sums[max_index]:
                max_index = i
            left[i] = max_index
        
        # Fill the right array
        max_index = len(sums) - 1
        for i in range(len(sums) - 1, -1, -1):
            if sums[i] >= sums[max_index]:  # Tie-breaking for lexicographical order
                max_index = i
            right[i] = max_index
        
        # Find the maximum sum by trying all middle intervals
        max_sum = 0
        result = []
        for mid in range(k, len(sums) - k):
            l = left[mid - k]
            r = right[mid + k]
            total = sums[l] + sums[mid] + sums[r]
            if total > max_sum:
                max_sum = total
                result = [l, mid, r]
        
        return result
