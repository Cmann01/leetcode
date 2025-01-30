from collections import deque, defaultdict
from typing import List

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Construct adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Find connected components and check if each is bipartite
        color = {}  # To store 0/1 for bipartiteness check
        components = []  # Store all connected components
        
        def is_bipartite(start):
            """Check if the component is bipartite and return the nodes in it."""
            queue = deque([start])
            component = set([start])
            color[start] = 0  # Start with color 0
            
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor in color:
                        # If colors conflict, graph is not bipartite
                        if color[neighbor] == color[node]:
                            return False, []
                    else:
                        color[neighbor] = 1 - color[node]  # Alternate color
                        queue.append(neighbor)
                        component.add(neighbor)
            return True, component

        # Step 3: Process all nodes, checking for bipartiteness
        visited = set()
        for node in range(1, n + 1):
            if node not in visited:
                bipartite, component = is_bipartite(node)
                if not bipartite:
                    return -1
                visited.update(component)
                components.append(component)

        # Step 4: Find the longest BFS depth in each component
        def bfs_max_depth(start):
            """Run BFS to find the maximum depth from any starting node."""
            queue = deque([start])
            visited = {start}
            depth = 0

            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                depth += 1  # Increase depth after each level
            return depth

        # Step 5: Compute the max depth for each component
        max_groups = 0
        for component in components:
            max_depth = 0
            for node in component:
                max_depth = max(max_depth, bfs_max_depth(node))
            max_groups += max_depth

        return max_groups
