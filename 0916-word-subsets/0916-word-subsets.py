from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Create a combined maximum frequency count for words2
        max_freq = Counter()
        for word in words2:
            freq = Counter(word)
            for char in freq:
                max_freq[char] = max(max_freq[char], freq[char])
        
        # Check each word in words1 to see if it satisfies the universal condition
        result = []
        for word in words1:
            freq = Counter(word)
            if all(freq[char] >= max_freq[char] for char in max_freq):
                result.append(word)
        
        return result
