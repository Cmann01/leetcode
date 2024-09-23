class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        # DP array, where dp[i] represents the minimum extra chars in the substring s[0:i]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Convert dictionary to a set for O(1) lookups
        word_set = set(dictionary)
        
        # Iterate over each index of the string s
        for i in range(1, n + 1):
            # Assume we don't use any word at index i-1
            dp[i] = dp[i - 1] + 1
            
            # Try to match any word in the dictionary ending at index i-1
            for word in word_set:
                length = len(word)
                if i >= length and s[i - length:i] == word:
                    dp[i] = min(dp[i], dp[i - length])
        
        # The answer is the minimum number of extra characters for the whole string s[0:n]
        return dp[n]
