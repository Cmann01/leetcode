class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        import math
        MOD = 10**9 + 7
        maxLen = 14  # maximum depth possible for divisibility chain

        # Precompute factorials and inverse factorials
        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = (fact[i - 1] * i) % MOD
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, 0, -1):
            inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

        def nCr(n, r):
            if r > n:
                return 0
            return (fact[n] * inv_fact[r] % MOD) * inv_fact[n - r] % MOD

        # dp[i][j]: number of ways to make a chain of length i ending in value j
        dp = [[0] * (maxValue + 1) for _ in range(maxLen + 1)]
        for i in range(1, maxValue + 1):
            dp[1][i] = 1

        for length in range(2, maxLen + 1):
            for val in range(1, maxValue + 1):
                for mul in range(2 * val, maxValue + 1, val):
                    dp[length][mul] = (dp[length][mul] + dp[length - 1][val]) % MOD

        result = 0
        for length in range(1, maxLen + 1):
            total = sum(dp[length]) % MOD
            result = (result + total * nCr(n - 1, length - 1)) % MOD

        return result
