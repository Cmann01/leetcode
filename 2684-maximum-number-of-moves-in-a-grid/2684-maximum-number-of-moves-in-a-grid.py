class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        
        max_moves = 0

        for j in range(n - 1):
            for i in range(m):
                if dp[i][j] > 0 or j == 0:
                    for di, dj in [(-1, 1), (0, 1), (1, 1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and nj < n and grid[ni][nj] > grid[i][j]:
                            dp[ni][nj] = max(dp[ni][nj], dp[i][j] + 1)
                            max_moves = max(max_moves, dp[ni][nj])

        return max_moves
