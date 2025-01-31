
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        island_sizes = {}
        index = 2  # Start indexing islands from 2 to differentiate from original 1s

        def dfs(r, c, index):
            stack = [(r, c)]
            grid[r][c] = index
            size = 1
            
            while stack:
                x, y = stack.pop()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = index
                        stack.append((nx, ny))
                        size += 1
            
            return size
        
        # Step 1: Identify and index all islands
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_sizes[index] = dfs(r, c, index)
                    index += 1
        
        # If the entire grid is one big island already
        if not island_sizes:
            return 1  # If grid has only zeros, changing one gives island size of 1
        
        max_island = max(island_sizes.values())
        
        # Step 2: Try flipping each 0 and checking the max island size
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    new_size = 1  # The flipped 0 counts as 1
                    
                    for dx, dy in directions:
                        nr, nc = r + dx, c + dy
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            island_index = grid[nr][nc]
                            if island_index not in seen:
                                seen.add(island_index)
                                new_size += island_sizes[island_index]
                    
                    max_island = max(max_island, new_size)
        
        return max_island