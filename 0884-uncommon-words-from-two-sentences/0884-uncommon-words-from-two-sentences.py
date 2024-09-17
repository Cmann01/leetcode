from collections import Counter
from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Split both sentences into words and combine them into a single list
        combined_words = s1.split() + s2.split()
        
        # Create a frequency count for all the words
        word_count = Counter(combined_words)
        
        # Return the words that appear exactly once
        return [word for word in word_count if word_count[word] == 1]
