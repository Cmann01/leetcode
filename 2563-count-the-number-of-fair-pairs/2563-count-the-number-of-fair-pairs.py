from typing import List
import bisect

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # Sort the array for efficient range finding
        nums.sort()
        n = len(nums)
        fair_pairs_count = 0

        # Iterate over each element as the first element of the pair
        for i in range(n):
            # Calculate bounds for the second element in the pair
            j_low = bisect.bisect_left(nums, lower - nums[i], i + 1)
            j_high = bisect.bisect_right(nums, upper - nums[i], i + 1) - 1

            # Add the count of valid pairs for this element
            fair_pairs_count += max(0, j_high - j_low + 1)

        return fair_pairs_count
