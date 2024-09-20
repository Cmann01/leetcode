class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Helper function to calculate LPS (Longest Prefix Suffix) array
        def computeLPS(pattern: str) -> list:
            lps = [0] * len(pattern)
            length = 0  # length of the previous longest prefix suffix
            i = 1
            
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        if not s or s == s[::-1]:  # If the string is already a palindrome
            return s
        
        rev_s = s[::-1]
        combined = s + "#" + rev_s
        lps = computeLPS(combined)
        
        # Find the part of the string that is not part of the palindrome
        suffix_length = len(s) - lps[-1]
        return rev_s[:suffix_length] + s

# Example usage:
solution = Solution()
print(solution.shortestPalindrome("aacecaaa"))  # Output: "aaacecaaa"
print(solution.shortestPalindrome("abcd"))      # Output: "dcbabcd"
