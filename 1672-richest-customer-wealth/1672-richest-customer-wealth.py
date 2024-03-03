class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0
        
        # Iterate through each customer's accounts and calculate their wealth
        for customer_accounts in accounts:
            wealth = sum(customer_accounts)
            max_wealth = max(max_wealth, wealth)  # Update max_wealth if current wealth is greater
        
        return max_wealth

# Example usage:
accounts1 = [[1,2,3],[3,2,1]]
accounts2 = [[1,5],[7,3],[3,5]]
accounts3 = [[2,8,7],[7,1,3],[1,9,5]]

solution = Solution()
print(solution.maximumWealth(accounts1))  # Output: 6
print(solution.maximumWealth(accounts2))  # Output: 10
print(solution.maximumWealth(accounts3))  # Output: 17
