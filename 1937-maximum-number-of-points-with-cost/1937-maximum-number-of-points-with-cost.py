class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = points[0]

        for r in range(1, m):
            left = [0] * n
            right = [0] * n
            
            # Compute the left pass
            left[0] = dp[0]
            for c in range(1, n):
                left[c] = max(left[c-1] - 1, dp[c])
            
            # Compute the right pass
            right[n-1] = dp[n-1]
            for c in range(n-2, -1, -1):
                right[c] = max(right[c+1] - 1, dp[c])
            
            # Update dp for the current row
            for c in range(n):
                dp[c] = points[r][c] + max(left[c], right[c])
        
        return max(dp)

# Example usage:
solution = Solution()
print(solution.maxPoints([[1,2,3],[1,5,1],[3,1,1]]))  # Output: 9
print(solution.maxPoints([[1,5],[2,3],[4,2]]))  # Output: 11
