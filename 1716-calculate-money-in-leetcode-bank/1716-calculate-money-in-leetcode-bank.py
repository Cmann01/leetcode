class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Calculate the number of complete weeks and the remaining days
        weeks = n // 7
        days = n % 7
        
        # Initialize the total money
        total = 0
        
        # Calculate the total money contributed by complete weeks
        # The total for complete weeks follows an arithmetic progression
        # where the first term is 1 and the common difference is the number
        # of completed weeks.
        total += 28 * weeks + 7 * (weeks - 1) * weeks // 2
        
        # Calculate the total money contributed by the remaining days
        # The additional money contributed on the first day of the week
        # is equal to the number of weeks.
        total += days * (days + 1) // 2 + weeks * days
        
        return total

# Test cases
solution = Solution()
print(solution.totalMoney(4))  # Output: 10
print(solution.totalMoney(10))  # Output: 37
print(solution.totalMoney(20))  # Output: 96
