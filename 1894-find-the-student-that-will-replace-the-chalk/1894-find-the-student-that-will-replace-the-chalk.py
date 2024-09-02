from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # Step 1: Calculate the total chalk usage in one round
        total_chalk = sum(chalk)
        
        # Step 2: Reduce k using modulo to avoid unnecessary full rounds
        k = k % total_chalk
        
        # Step 3: Find the student who will replace the chalk
        for i, chalk_needed in enumerate(chalk):
            if k < chalk_needed:
                return i
            k -= chalk_needed
