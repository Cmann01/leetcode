class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # If k is greater than the length of s, it's impossible to create k palindromes
        if k > len(s):
            return False
        
        # Count the frequency of each character
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Count the number of characters with an odd frequency
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
        
        # To form k palindromes, we need at least odd_count <= k
        return odd_count <= k
