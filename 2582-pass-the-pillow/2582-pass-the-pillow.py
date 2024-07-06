class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # Length of one complete cycle
        cycle_length = 2 * (n - 1)
        
        # Position within the cycle
        position_in_cycle = time % cycle_length
        
        # Determine the actual position
        if position_in_cycle < n:
            # Moving forward
            return position_in_cycle + 1
        else:
            # Moving backward
            return n - (position_in_cycle - n + 1)

# Example usage
solution = Solution()
print(solution.passThePillow(4, 5))  # Output: 2
print(solution.passThePillow(3, 2))  # Output: 3
