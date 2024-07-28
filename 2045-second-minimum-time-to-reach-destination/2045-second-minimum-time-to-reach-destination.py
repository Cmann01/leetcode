from collections import defaultdict, deque
from heapq import heappush, heappop
from typing import List

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        d1 = [float('inf')] * (n + 1)
        d2 = [float('inf')] * (n + 1)
        pq = []
        heappush(pq, (0, 1))  # (timePassed, node)
        d1[1] = 0

        while pq:
            timePassed, node = heappop(pq)

            if d2[n] != float('inf') and node == n:
                return d2[n]

            mult = timePassed // change
            if mult % 2 == 1:  # Red light
                timePassed = change * (mult + 1)  # Wait for green light

            for nbr in adj[node]:
                if d1[nbr] > timePassed + time:  # Found a shorter path
                    d2[nbr] = d1[nbr]
                    d1[nbr] = timePassed + time
                    heappush(pq, (timePassed + time, nbr))
                elif d2[nbr] > timePassed + time and d1[nbr] != timePassed + time:
                    d2[nbr] = timePassed + time
                    heappush(pq, (timePassed + time, nbr))

        return -1

# Test cases
sol = Solution()

# Case 1
n1 = 2
edges1 = [[1, 2]]
time1 = 3
change1 = 2
print(sol.secondMinimum(n1, edges1, time1, change1))  # Expected: 11

# Case 2
n2 = 5
edges2 = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
time2 = 3
change2 = 5
print(sol.secondMinimum(n2, edges2, time2, change2))  # Expected: 13
