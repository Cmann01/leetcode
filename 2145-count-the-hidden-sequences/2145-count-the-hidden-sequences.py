from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_prefix_sum = 0
        max_prefix_sum = 0
        curr = 0

        for diff in differences:
            curr += diff
            min_prefix_sum = min(min_prefix_sum, curr)
            max_prefix_sum = max(max_prefix_sum, curr)

        min_start = lower - min_prefix_sum
        max_start = upper - max_prefix_sum

        return max(0, max_start - min_start + 1)
