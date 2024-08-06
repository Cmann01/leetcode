class Solution:
    def minimumPushes(self, word: str) -> int:
        from collections import Counter
        
        # Count the frequency of each letter in the word
        frequency = Counter(word)
        
        # Get the frequencies sorted in descending order
        sorted_frequencies = sorted(frequency.values(), reverse=True)
        
        # Calculate the minimum number of presses
        presses = 0
        for i, freq in enumerate(sorted_frequencies):
            presses += freq * ((i // 8) + 1)
        
        return presses

# Example usage:
sol = Solution()
print(sol.minimumPushes("abcde"))           # Output: 5
print(sol.minimumPushes("xyzxyzxyzxyz"))    # Output: 12
print(sol.minimumPushes("aabbccddeeffgghhiiiiii"))  # Output: 24
