class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        # Convert banned list to a set for O(1) lookup
        banned_set = set(banned)
        
        # Initialize variables
        current_sum = 0
        count = 0
        
        # Iterate through integers from 1 to n
        for i in range(1, n + 1):
            # Skip if the number is in the banned set
            if i in banned_set:
                continue
            
            # Check if adding the current number exceeds maxSum
            if current_sum + i > maxSum:
                break
            
            # Add the current number to the sum and increment the count
            current_sum += i
            count += 1
        
        return count
