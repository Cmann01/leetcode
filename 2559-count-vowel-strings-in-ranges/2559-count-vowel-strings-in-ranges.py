class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Define vowels
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Helper function to check if a string starts and ends with a vowel
        def is_vowel_string(word):
            return word[0] in vowels and word[-1] in vowels
        
        # Create a prefix sum array
        n = len(words)
        prefix = [0] * (n + 1)  # prefix[i] stores the count of vowel strings in words[:i]
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if is_vowel_string(words[i]) else 0)
        
        # Answer each query using the prefix sum
        ans = []
        for li, ri in queries:
            # Number of vowel strings in the range [li, ri]
            ans.append(prefix[ri + 1] - prefix[li])
        
        return ans
