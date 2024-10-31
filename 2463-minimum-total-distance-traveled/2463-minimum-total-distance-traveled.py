from typing import List

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Sort robots and factories by position
        robot.sort()
        factory.sort()
        
        n, m = len(robot), len(factory)
        
        # Initialize DP table with infinity
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0  # No robots, no factories -> 0 distance
        
        # DP transition
        for i in range(n + 1):  # Loop over robots
            for j in range(m):  # Loop over factories
                pos, limit = factory[j]
                distance_sum = 0
                
                # Loop to assign k robots to j-th factory
                for k in range(min(limit, n - i) + 1):
                    # Accumulate distance for current allocation of `k` robots to `j`-th factory
                    if k > 0:
                        distance_sum += abs(robot[i + k - 1] - pos)
                    dp[i + k][j + 1] = min(dp[i + k][j + 1], dp[i][j] + distance_sum)
        
        # The answer will be the minimum distance to repair all robots across all factories
        return min(dp[n][j] for j in range(m + 1))
