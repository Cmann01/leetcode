class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        # Suffix sum array
        suffixSum = [0] * n
        suffixSum[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffixSum[i] = piles[i] + suffixSum[i + 1]
        
        # DP array
        dp = [[0] * (n + 1) for _ in range(n)]
        
        # Bottom-up DP
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                # When Alice can take all remaining piles
                if i + 2 * m >= n:
                    dp[i][m] = suffixSum[i]
                else:
                    # Try to take x piles where 1 <= x <= 2m
                    dp[i][m] = max(suffixSum[i] - dp[i + x][max(m, x)] for x in range(1, 2 * m + 1))
        
        return dp[0][1]  # Starting from index 0 with M = 1
