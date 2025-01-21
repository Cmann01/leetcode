from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        # Compute prefix and suffix sums for both rows
        top_suffix = [0] * n
        bottom_prefix = [0] * n
        
        # Suffix sum for the top row
        top_suffix[n-1] = grid[0][n-1]
        for i in range(n-2, -1, -1):
            top_suffix[i] = top_suffix[i+1] + grid[0][i]
        
        # Prefix sum for the bottom row
        bottom_prefix[0] = grid[1][0]
        for i in range(1, n):
            bottom_prefix[i] = bottom_prefix[i-1] + grid[1][i]
        
        # Find the minimum possible score for the second robot
        min_second_robot_score = float('inf')
        
        for c in range(n):
            # Calculate the maximum score the second robot can get
            score_top = top_suffix[c+1] if c + 1 < n else 0
            score_bottom = bottom_prefix[c-1] if c - 1 >= 0 else 0
            second_robot_score = max(score_top, score_bottom)
            
            # Update the minimum score the second robot can get
            min_second_robot_score = min(min_second_robot_score, second_robot_score)
        
        return min_second_robot_score
