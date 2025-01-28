from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            # If out of bounds or the cell is land (0), return 0
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 0:
                return 0
            
            # Catch all the fish in the current cell
            fish_count = grid[r][c]
            
            # Mark the cell as visited by setting it to 0
            grid[r][c] = 0
            
            # Explore all 4 possible directions and sum up fish from connected cells
            for dr, dc in directions:
                fish_count += dfs(r + dr, c + dc)
            
            return fish_count
        
        # Get the dimensions of the grid
        m, n = len(grid), len(grid[0])
        
        # Define the 4 possible movement directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        max_fish = 0
        
        # Iterate through all cells in the grid
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:  # Start DFS from each water cell
                    max_fish = max(max_fish, dfs(r, c))
        
        return max_fish
