from heapq import heappush, heappop
from typing import List

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # If both initial moves require more than 1 second, return -1
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        
        visited = [[False] * n for _ in range(m)]
        result = [[float('inf')] * n for _ in range(m)]
        result[0][0] = 0
        
        # Priority queue (min-heap): (time, row, col)
        pq = [(grid[0][0], 0, 0)]
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while pq:
            time, row, col = heappop(pq)
            
            # If we reached the bottom-right cell
            if (row, col) == (m - 1, n - 1):
                return result[m - 1][n - 1]
            
            # Skip if already visited
            if visited[row][col]:
                continue
            visited[row][col] = True
            
            # Explore neighbors
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and not visited[r][c]:
                    if grid[r][c] <= time + 1:
                        next_time = time + 1
                    elif (grid[r][c] - time) % 2 == 0:
                        next_time = grid[r][c] + 1
                    else:
                        next_time = grid[r][c]
                    
                    if next_time < result[r][c]:
                        result[r][c] = next_time
                        heappush(pq, (next_time, r, c))
        
        return -1
