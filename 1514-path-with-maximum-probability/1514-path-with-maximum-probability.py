import heapq
from collections import defaultdict
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # Create graph representation using an adjacency list
        graph = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))
        
        # Priority queue for Dijkstra-like traversal, starting with (probability, start node)
        max_heap = [(-1.0, start)]  # Start with probability of 1.0, stored as -1.0
        # Max probability to reach each node
        max_prob = [0.0] * n
        max_prob[start] = 1.0
        
        while max_heap:
            # Get the node with the highest probability
            current_prob, node = heapq.heappop(max_heap)
            current_prob = -current_prob  # Convert back to positive
            
            # If we reached the end node, return the probability
            if node == end:
                return current_prob
            
            # Update neighbors
            for neighbor, edge_prob in graph[node]:
                new_prob = current_prob * edge_prob
                # If a higher probability path is found, update and push to the heap
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))
        
        # If end is unreachable, return 0
        return 0.0
