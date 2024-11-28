from collections import deque
from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Initialize the adjacency list for the graph
        graph = {i: [] for i in range(n)}
        for i in range(n - 1):
            graph[i].append(i + 1)
        
        def bfs_shortest_path():
            """BFS to find the shortest path from 0 to n-1."""
            queue = deque([(0, 0)])  # (current node, distance)
            visited = set()
            while queue:
                node, dist = queue.popleft()
                if node == n - 1:
                    return dist
                if node in visited:
                    continue
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, dist + 1))
            return float('inf')  # If no path exists
        
        # Process queries
        results = []
        for u, v in queries:
            graph[u].append(v)  # Add the new road
            results.append(bfs_shortest_path())
        
        return results
