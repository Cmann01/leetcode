from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        # Step 1: Calculate the base satisfaction from customers who are always satisfied
        always_satisfied = sum(customers[i] for i in range(n) if grumpy[i] == 0)
        
        # Step 2: Calculate the maximum additional satisfaction during the grumpy minutes using a sliding window
        max_additional_satisfaction = 0
        current_additional_satisfaction = 0
        
        # Initial window calculation
        for i in range(minutes):
            if grumpy[i] == 1:
                current_additional_satisfaction += customers[i]
        
        max_additional_satisfaction = current_additional_satisfaction
        
        # Sliding the window across the array
        for i in range(minutes, n):
            if grumpy[i] == 1:
                current_additional_satisfaction += customers[i]
            if grumpy[i - minutes] == 1:
                current_additional_satisfaction -= customers[i - minutes]
            
            max_additional_satisfaction = max(max_additional_satisfaction, current_additional_satisfaction)
        
        # Step 3: The result is the sum of always satisfied and the maximum additional satisfaction
        return always_satisfied + max_additional_satisfaction

# Example usage
solution = Solution()
print(solution.maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3))  # Output: 16
print(solution.maxSatisfied([1], [0], 1))  # Output: 1
