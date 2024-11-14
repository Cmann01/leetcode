from typing import List
import math

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # Helper function to check if a maximum per store of `x` is feasible
        def can_distribute(x):
            required_stores = 0
            for quantity in quantities:
                required_stores += math.ceil(quantity / x)
            return required_stores <= n

        # Binary search for the minimal maximum
        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            if can_distribute(mid):
                right = mid  # Try for a smaller maximum
            else:
                left = mid + 1  # Increase the maximum

        return left
