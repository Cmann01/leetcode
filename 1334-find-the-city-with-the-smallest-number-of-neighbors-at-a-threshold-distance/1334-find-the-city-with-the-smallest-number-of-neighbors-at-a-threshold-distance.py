class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize the distance matrix with infinity
        dist = [[float('inf')] * n for _ in range(n)]
        
        # Distance from a city to itself is always 0
        for i in range(n):
            dist[i][i] = 0
        
        # Populate the initial distances based on the edges given
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Floyd-Warshall Algorithm to find all pairs shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Determine the number of reachable cities for each city
        min_reachable = n
        result_city = -1
        
        for i in range(n):
            reachable_count = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
            if reachable_count < min_reachable or (reachable_count == min_reachable and i > result_city):
                min_reachable = reachable_count
                result_city = i
        
        return result_city

# Example usage:
# sol = Solution()
# print(sol.findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4))  # Output: 3
# print(sol.findTheCity(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2))  # Output: 0
