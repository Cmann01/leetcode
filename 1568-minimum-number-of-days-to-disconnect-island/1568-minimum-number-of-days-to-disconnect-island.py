class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def count_islands(grid):
            # Helper function to count the number of islands
            def dfs(i, j):
                if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                    return
                grid[i][j] = 0
                for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    dfs(i + x, j + y)
            
            count = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        count += 1
                        dfs(i, j)
            return count
        
        def is_disconnected(grid):
            return count_islands([row[:] for row in grid]) != 1
        
        if is_disconnected(grid):
            return 0
        
        # Check if removing one cell can disconnect the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if is_disconnected(grid):
                        return 1
                    grid[i][j] = 1
        
        # Check if removing two cells can disconnect the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    for x in range(len(grid)):
                        for y in range(len(grid[0])):
                            if grid[x][y] == 1:
                                grid[x][y] = 0
                                if is_disconnected(grid):
                                    return 2
                                grid[x][y] = 1
                    grid[i][j] = 1
        
        return 2
