class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        
        # Forward traversal (Approach 1)
        swap = 0
        black = 0
        
        for i in range(n):
            if s[i] == '0':  # Move white to the left
                swap += black
            else:  # It's a '1', increment black count
                black += 1
        
        return swap

# Instantiate the Solution class and call the method
test_case = "100"
solution = Solution()
print(solution.minimumSteps(test_case))  # Output: 2
