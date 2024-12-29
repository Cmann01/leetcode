from collections import Counter
from functools import lru_cache

class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        MOD = 10**9 + 7
        m, n = len(words), len(words[0])  # m: number of words, n: length of each word

        # Step 1: Precompute frequency of characters in each column
        char_count = [Counter() for _ in range(n)]
        for word in words:
            for col, char in enumerate(word):
                char_count[col][char] += 1

        # Step 2: Define DP function
        @lru_cache(None)
        def dp(i, j):
            # Base Case: If target is fully formed
            if i == len(target):
                return 1
            # If columns are exhausted
            if j == n:
                return 0
            
            # Option 1: Skip this column
            result = dp(i, j + 1) % MOD
            
            # Option 2: Use this column if possible
            target_char = target[i]
            if target_char in char_count[j]:
                result += char_count[j][target_char] * dp(i + 1, j + 1)
                result %= MOD
            
            return result
        
        # Compute the result
        return dp(0, 0)
