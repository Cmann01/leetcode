from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        
        # Step 1: Build the adjacency list
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        # Step 2: Find all connected components using DFS
        visited = set()
        complete_count = 0
        
        def dfs(node, component):
            stack = [node]
            while stack:
                curr = stack.pop()
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
                        component.add(neighbor)
        
        for i in range(n):
            if i not in visited:
                visited.add(i)
                component = {i}
                dfs(i, component)
                
                # Step 3: Check if the component is complete
                size = len(component)
                is_complete = all(len(graph[node]) == size - 1 for node in component)
                
                if is_complete:
                    complete_count += 1
        
        return complete_count