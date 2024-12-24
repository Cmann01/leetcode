from collections import deque
from typing import List

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        # Helper function to find the farthest node and its distance using BFS
        def bfs_find_farthest(node: int, graph: List[List[int]]) -> (int, int):
            visited = set()
            queue = deque([(node, 0)])
            visited.add(node)
            farthest_node, max_distance = node, 0
            
            while queue:
                current, distance = queue.popleft()
                if distance > max_distance:
                    farthest_node, max_distance = current, distance
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, distance + 1))
            
            return farthest_node, max_distance

        # Helper function to calculate the diameter of a tree
        def calculate_diameter(edges: List[List[int]], n: int) -> (int, int):
            graph = [[] for _ in range(n)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            
            # First BFS to find the farthest node
            farthest_node, _ = bfs_find_farthest(0, graph)
            # Second BFS to find the diameter and the maximum depth
            farthest_node2, diameter = bfs_find_farthest(farthest_node, graph)
            return diameter, (diameter + 1) // 2

        # Number of nodes in the trees
        n1 = len(edges1) + 1
        n2 = len(edges2) + 1

        # Calculate the diameters of the two trees and their "radius"
        diameter1, radius1 = calculate_diameter(edges1, n1)
        diameter2, radius2 = calculate_diameter(edges2, n2)

        # Calculate the minimum possible diameter after connecting the two trees
        min_diameter = max(diameter1, diameter2, radius1 + radius2 + 1)
        return min_diameter
