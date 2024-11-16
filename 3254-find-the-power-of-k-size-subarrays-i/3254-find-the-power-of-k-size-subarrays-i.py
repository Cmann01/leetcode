from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [-1] * (n - k + 1)  # Initialize the result array with -1
        count = 1  # Count of consecutive elements

        # Preprocess the first window
        for i in range(1, k):
            if nums[i] == nums[i - 1] + 1:
                count += 1
            else:
                count = 1

        # Check if the first window satisfies the condition
        if count == k:
            result[0] = nums[k - 1]

        i, j = 1, k

        # Process the sliding window
        while j < n:
            if nums[j] == nums[j - 1] + 1:
                count += 1
            else:
                count = 1

            if count >= k:
                result[i] = nums[j]

            i += 1
            j += 1

        return result
