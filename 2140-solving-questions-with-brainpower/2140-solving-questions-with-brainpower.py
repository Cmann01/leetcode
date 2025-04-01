from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  # dp[i] represents the max points from index i to end
        
        for i in range(n - 1, -1, -1):  # Process from last question to first
            points, brainpower = questions[i]
            next_index = i + brainpower + 1  # Next question that can be solved if this one is chosen
            
            # If next_index is within bounds, add its dp value, else consider only current points
            dp[i] = max(points + (dp[next_index] if next_index < n else 0), dp[i + 1])
        
        return dp[0]