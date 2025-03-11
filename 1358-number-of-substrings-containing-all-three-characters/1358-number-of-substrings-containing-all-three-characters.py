class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = { 'a': 0, 'b': 0, 'c': 0 }  # Dictionary to track character count
        left = 0  # Left pointer
        res = 0   # Result counter

        for right in range(len(s)):  # Right pointer iterates over the string
            count[s[right]] += 1  # Include current character in the window

            while all(count[char] > 0 for char in 'abc'):  # Check if all chars are present
                res += len(s) - right  # Count valid substrings
                count[s[left]] -= 1  # Move left pointer to shrink window
                left += 1
        
        return res
