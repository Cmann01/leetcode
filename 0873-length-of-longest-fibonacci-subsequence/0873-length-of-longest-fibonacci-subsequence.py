from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {x: i for i, x in enumerate(arr)}  # Mapping value to index
        n = len(arr)
        dp = {}  # Dictionary to store longest fib-like subsequence ending at (i, j)
        max_length = 0
        
        for j in range(n):
            for i in range(j):
                x = arr[j] - arr[i]  # Previous number needed to form Fibonacci-like sequence
                if x < arr[i] and x in index:
                    k = index[x]  # Index of x in the array
                    dp[i, j] = dp.get((k, i), 2) + 1
                    max_length = max(max_length, dp[i, j])
        
        return max_length if max_length >= 3 else 0
