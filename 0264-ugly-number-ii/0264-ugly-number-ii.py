class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Initialize dp array where dp[i] will store the i-th ugly number
        dp = [0] * n
        dp[0] = 1  # The first ugly number is 1
        
        # Pointers for 2, 3, and 5
        i2 = i3 = i5 = 0
        
        # Initial multiples
        next_2 = 2
        next_3 = 3
        next_5 = 5
        
        for i in range(1, n):
            # The next ugly number is the minimum of these multiples
            dp[i] = min(next_2, next_3, next_5)
            
            # Move the pointer(s) forward that matched the minimum
            if dp[i] == next_2:
                i2 += 1
                next_2 = dp[i2] * 2
            if dp[i] == next_3:
                i3 += 1
                next_3 = dp[i3] * 3
            if dp[i] == next_5:
                i5 += 1
                next_5 = dp[i5] * 5
        
        # The n-th ugly number is the last one in the dp array
        return dp[-1]
