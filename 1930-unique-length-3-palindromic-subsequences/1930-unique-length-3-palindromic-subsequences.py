class Solution:
    def countPalindromicSubsequence(self, s):
        first = [-1] * 26  # To store the first occurrence of each character
        last = [-1] * 26   # To store the last occurrence of each character
        
        # Step 1: Track the first and last occurrence of each character
        for i in range(len(s)):
            curr = ord(s[i]) - ord("a")
            if first[curr] == -1:
                first[curr] = i
            last[curr] = i
        
        ans = 0
        # Step 2: Iterate through each character and calculate the number of distinct palindromic subsequences
        for i in range(26):
            if first[i] == -1:
                continue  # Skip characters that do not exist in the string
                
            # Set to track distinct characters between the first and last occurrence
            between = set()
            for j in range(first[i] + 1, last[i]):
                between.add(s[j])
            
            # Each distinct character forms a unique palindromic subsequence
            ans += len(between)

        return ans
