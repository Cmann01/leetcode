class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        # dp[i][j] represents the minimum number of turns needed to print the substring s[i:j+1]
        dp = [[0] * n for _ in range(n)]
        
        # Fill the DP table
        for length in range(1, n + 1):  # length of the substring
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = length  # maximum turns: printing one character at a time
                for k in range(i, j):
                    # If characters are same, we can reduce the turns
                    if s[k] == s[j]:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] - 1)
                    else:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
        
        return dp[0][n-1]
