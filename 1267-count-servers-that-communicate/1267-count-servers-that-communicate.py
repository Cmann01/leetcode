from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # Get the dimensions of the grid
        m, n = len(grid), len(grid[0])
        
        # Count the number of servers in each row and each column
        row_count = [0] * m
        col_count = [0] * n
        
        # Iterate over the grid to populate row_count and col_count
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
                    
        # Count the servers that can communicate with at least one other server
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    result += 1
                    
        return result
