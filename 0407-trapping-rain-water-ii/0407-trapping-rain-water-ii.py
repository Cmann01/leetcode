import heapq
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        min_heap = []
        water_trapped = 0

        # Add all the border cells to the min-heap and mark them as visited
        for i in range(m):
            for j in [0, n - 1]:  # First and last column
                heapq.heappush(min_heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(n):
            for i in [0, m - 1]:  # First and last row
                heapq.heappush(min_heap, (heightMap[i][j], i, j))
                visited[i][j] = True

        # Directions for the 4 neighboring cells
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Process cells in the min-heap
        while min_heap:
            height, x, y = heapq.heappop(min_heap)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    # Calculate water trapped for this cell
                    water_trapped += max(0, height - heightMap[nx][ny])
                    # Add the cell to the heap with the max height between current and new cell
                    heapq.heappush(min_heap, (max(height, heightMap[nx][ny]), nx, ny))

        return water_trapped
