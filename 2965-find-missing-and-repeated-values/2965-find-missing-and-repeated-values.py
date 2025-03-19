from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        num_count = {}  # Dictionary to track occurrences of numbers
        
        # Flatten grid and count occurrences
        for row in grid:
            for num in row:
                num_count[num] = num_count.get(num, 0) + 1
        
        repeated, missing = -1, -1
        
        # Check which number is missing and which is repeated
        for num in range(1, n * n + 1):
            if num_count.get(num, 0) == 2:
                repeated = num
            elif num_count.get(num, 0) == 0:
                missing = num
        
        return [repeated, missing]
