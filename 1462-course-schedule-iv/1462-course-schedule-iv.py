from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Initialize the adjacency matrix
        reachable = [[False] * numCourses for _ in range(numCourses)]
        
        # Fill in the direct prerequisites
        for a, b in prerequisites:
            reachable[a][b] = True
        
        # Floyd-Warshall Algorithm for transitive closure
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])
        
        # Answer each query
        result = []
        for u, v in queries:
            result.append(reachable[u][v])
        
        return result
