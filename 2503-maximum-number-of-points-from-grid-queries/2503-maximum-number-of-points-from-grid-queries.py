from heapq import heappop, heappush
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        q_sorted = sorted(enumerate(queries), key=lambda x: x[1])
        result = [0] * len(queries)
        visited = [[False] * n for _ in range(m)]
        
        min_heap = [(grid[0][0], 0, 0)]  # (value, x, y)
        visited[0][0] = True
        count = 0
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for i, query in q_sorted:
            while min_heap and min_heap[0][0] < query:
                val, x, y = heappop(min_heap)
                count += 1  # We can visit this cell
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        heappush(min_heap, (grid[nx][ny], nx, ny))
                        visited[nx][ny] = True
            
            result[i] = count
        
        return result
