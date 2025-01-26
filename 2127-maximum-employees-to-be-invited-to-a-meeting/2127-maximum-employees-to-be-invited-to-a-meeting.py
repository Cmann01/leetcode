from collections import defaultdict, deque
from typing import List

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        in_degree = [0] * n
        for f in favorite:
            in_degree[f] += 1

        # Topological sort to find chains
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        chain_length = [0] * n
        while queue:
            node = queue.popleft()
            next_node = favorite[node]
            chain_length[next_node] = max(chain_length[next_node], chain_length[node] + 1)
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                queue.append(next_node)

        # Find cycles
        visited = [False] * n
        max_cycle_size = 0
        total_chains_in_2_cycles = 0

        for i in range(n):
            if not visited[i] and in_degree[i] > 0:  # Only start from nodes in cycles
                cycle_size = 0
                current = i
                # Traverse the cycle
                while not visited[current]:
                    visited[current] = True
                    cycle_size += 1
                    current = favorite[current]
                
                if cycle_size == 2:
                    # Handle 2-cycle
                    total_chains_in_2_cycles += (
                        chain_length[i] + chain_length[favorite[i]] + 2
                    )
                else:
                    # Handle larger cycles
                    max_cycle_size = max(max_cycle_size, cycle_size)

        return max(max_cycle_size, total_chains_in_2_cycles)
