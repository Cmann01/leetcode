class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        # Step 1: Initialize in-degrees
        in_degree = [0] * n
        
        # Step 2: Calculate in-degree for each node
        for u, v in edges:
            in_degree[v] += 1
        
        champ = -1
        count = 0
        
        # Step 3: Check for the champion node
        for i in range(n):
            if in_degree[i] == 0:  # ith node is a potential champion
                champ = i
                count += 1
                if count > 1:  # More than one node with in-degree 0
                    return -1
        
        return champ
