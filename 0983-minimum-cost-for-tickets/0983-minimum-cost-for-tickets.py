from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Create a DP array where dp[i] represents the minimum cost to cover up to day i
        dp = [0] * (days[-1] + 1)  # We only care about days up to the last travel day
        travel_days = set(days)  # To quickly check if a day is a travel day

        for i in range(1, days[-1] + 1):
            if i not in travel_days:  # If not a travel day, cost remains the same as the previous day
                dp[i] = dp[i - 1]
            else:
                # Consider the cost of a 1-day pass, 7-day pass, and 30-day pass
                cost1 = dp[i - 1] + costs[0]  # 1-day pass
                cost7 = dp[max(0, i - 7)] + costs[1]  # 7-day pass
                cost30 = dp[max(0, i - 30)] + costs[2]  # 30-day pass
                # Take the minimum of these three options
                dp[i] = min(cost1, cost7, cost30)

        return dp[days[-1]]  # The cost to cover up to the last travel day
