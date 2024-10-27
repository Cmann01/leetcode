from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # Dimensions of the matrix
        m, n = len(matrix), len(matrix[0])
        
        # Initialize the dp matrix with the same size as matrix
        dp = [[0] * n for _ in range(m)]
        total_squares = 0
        
        for i in range(m):
            for j in range(n):
                # Only process cells with 1s
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1  # First row or first column
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    
                    # Accumulate count of squares
                    total_squares += dp[i][j]
        
        return total_squares
