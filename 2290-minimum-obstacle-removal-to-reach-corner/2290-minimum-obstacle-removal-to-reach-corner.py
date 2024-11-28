from collections import deque
from typing import List

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Distance matrix initialized to infinity
        distance = [[float('inf')] * n for _ in range(m)]
        distance[0][0] = 0
        
        # Deque for 0-1 BFS
        dq = deque([(0, 0, 0)])  # (cost, row, col)
        
        while dq:
            cost, x, y = dq.popleft()
            
            # If we've reached the bottom-right corner
            if x == m - 1 and y == n - 1:
                return cost
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check bounds
                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = cost + grid[nx][ny]
                    
                    # Update distance if we find a better path
                    if new_cost < distance[nx][ny]:
                        distance[nx][ny] = new_cost
                        if grid[nx][ny] == 0:
                            dq.appendleft((new_cost, nx, ny))  # Free cell, prioritize it
                        else:
                            dq.append((new_cost, nx, ny))  # Obstacle, process later
        
        return -1  # If no path exists (though the problem guarantees one)

