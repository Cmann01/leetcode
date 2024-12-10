class Solution:
    def maximumLength(self, s: str) -> int:
        def is_special(sub):
            return len(set(sub)) == 1  # All characters in the substring are the same
        
        n = len(s)
        max_length = -1
        
        # Iterate through all possible lengths of substrings
        for length in range(1, n + 1):
            freq = {}
            
            # Iterate through all substrings of the current length
            for i in range(n - length + 1):
                substring = s[i:i + length]
                if is_special(substring):
                    freq[substring] = freq.get(substring, 0) + 1
            
            # Check if any special substring occurs at least 3 times
            for sub, count in freq.items():
                if count >= 3:
                    max_length = max(max_length, len(sub))
        
        return max_length

# Example usage:
solution = Solution()
print(solution.maximumLength("aaaa"))  # Output: 2
print(solution.maximumLength("abcdef"))  # Output: -1
print(solution.maximumLength("abcaba"))  # Output: 1
