from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        count = 0  # count of max_val in current window
        left = 0
        result = 0

        for right in range(len(nums)):
            if nums[right] == max_val:
                count += 1

            # Shrink window until we have exactly (or more) k max_vals
            while count >= k:
                # All subarrays from left to right are valid
                result += len(nums) - right

                # Shrink window from the left
                if nums[left] == max_val:
                    count -= 1
                left += 1

        return result
