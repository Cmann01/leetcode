class Solution:
    def maxScore(self, s: str) -> int:
        # Initialize variables to store the maximum score
        max_score = 0
        
        # Iterate through all possible split points, excluding the last character
        for i in range(1, len(s)):
            # Split the string into left and right substrings
            left = s[:i]
            right = s[i:]
            
            # Calculate the score: zeros in left + ones in right
            score = left.count('0') + right.count('1')
            
            # Update the maximum score
            max_score = max(max_score, score)
        
        return max_score
