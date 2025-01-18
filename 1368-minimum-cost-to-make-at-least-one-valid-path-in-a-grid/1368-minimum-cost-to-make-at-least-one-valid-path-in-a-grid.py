import heapq

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Directions: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Priority queue: (cost, x, y)
        pq = [(0, 0, 0)]  # Start at (0, 0) with cost 0
        visited = set()   # Track visited cells
        
        while pq:
            cost, x, y = heapq.heappop(pq)
            
            # If we reach the bottom-right cell, return the cost
            if (x, y) == (m-1, n-1):
                return cost
            
            # Skip if already visited
            if (x, y) in visited:
                continue
            visited.add((x, y))
            
            # Explore all 4 possible directions
            for d, (dx, dy) in enumerate(directions, start=1):
                nx, ny = x + dx, y + dy
                
                # Ensure the new position is within bounds
                if 0 <= nx < m and 0 <= ny < n:
                    # If the direction matches the current cell, no cost
                    new_cost = cost if grid[x][y] == d else cost + 1
                    heapq.heappush(pq, (new_cost, nx, ny))
        
        return -1  # Should never reach here if a path exists
