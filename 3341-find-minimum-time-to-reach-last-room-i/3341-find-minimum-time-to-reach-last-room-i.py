import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result = [[float('inf')] * n for _ in range(m)]
        result[0][0] = 0

        pq = [(0, 0, 0)]  # (currTime, i, j)

        while pq:
            currTime, i, j = heapq.heappop(pq)

            if i == m - 1 and j == n - 1:
                return currTime

            for dx, dy in directions:
                i_, j_ = i + dx, j + dy

                if 0 <= i_ < m and 0 <= j_ < n:
                    wait = max(moveTime[i_][j_] - currTime, 0)
                    arrTime = currTime + wait + 1

                    if result[i_][j_] > arrTime:
                        result[i_][j_] = arrTime
                        heapq.heappush(pq, (arrTime, i_, j_))

        return -1
