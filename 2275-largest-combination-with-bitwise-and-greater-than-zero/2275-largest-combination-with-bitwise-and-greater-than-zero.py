from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_count = 0
        
        # We will only check up to 24 bits (for numbers up to 10^7)
        for bit_position in range(24):
            count = 0
            for number in candidates:
                # Check if the bit at `bit_position` is set in `number`
                if number & (1 << bit_position):
                    count += 1
            # Update the maximum count
            max_count = max(max_count, count)
        
        return max_count
