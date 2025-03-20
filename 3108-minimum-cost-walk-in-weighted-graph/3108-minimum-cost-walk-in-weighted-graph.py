from heapq import heappop, heappush
from typing import List
from collections import defaultdict

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Step 1: Construct graph as adjacency list
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Step 2: Compute the minimum bitwise AND walk cost using BFS (Dijkstra-like approach)
        def bfs(start):
            # Min heap (priority queue) -> (cost, node)
            INF = 0xFFFFFFFF  # Large bitmask instead of float('inf')
            heap = [(INF, start)]
            min_cost = {i: INF for i in range(n)}
            min_cost[start] = INF
            
            while heap:
                cost, node = heappop(heap)
                
                # Explore neighbors
                for neighbor, weight in graph[node]:
                    new_cost = cost & weight  # Compute the AND cost
                    
                    # If a better AND-cost is found, update and push to the heap
                    if new_cost < min_cost[neighbor]:
                        min_cost[neighbor] = new_cost
                        heappush(heap, (new_cost, neighbor))
            
            return min_cost
        
        # Step 3: Precompute shortest AND paths for all nodes
        precomputed = {i: bfs(i) for i in range(n)}
        
        # Step 4: Process queries
        result = []
        for s, t in queries:
            cost = precomputed[s].get(t, 0xFFFFFFFF)
            result.append(cost if cost != 0xFFFFFFFF else -1)
        
        return result
