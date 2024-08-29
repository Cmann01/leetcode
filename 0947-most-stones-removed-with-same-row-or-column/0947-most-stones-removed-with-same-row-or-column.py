class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Create a dictionary to track the stones in the same row or column
        graph = {}
        
        # Function to add edges between stones sharing the same row or column
        def add_edge(x, y):
            if x not in graph:
                graph[x] = []
            graph[x].append(y)
        
        # Map stones by their row and column to create edges in the graph
        for x, y in stones:
            add_edge(x, ~y)  # ~y is used to differentiate row and column nodes
            add_edge(~y, x)
        
        # Function to perform DFS and count connected components
        def dfs(node):
            stack = [node]
            while stack:
                current = stack.pop()
                if current in visited:
                    continue
                visited.add(current)
                stack.extend(graph[current])
        
        # Track visited nodes
        visited = set()
        components = 0
        
        # Perform DFS for each node in the graph
        for x, y in stones:
            if x not in visited:
                components += 1
                dfs(x)
        
        # The maximum number of stones that can be removed is the total stones minus the number of components
        return len(stones) - components
