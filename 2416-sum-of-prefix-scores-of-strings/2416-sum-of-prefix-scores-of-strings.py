class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0  # To count how many words share this prefix

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # Step 1: Build the Trie
        root = TrieNode()
        
        # Insert each word into the Trie
        for word in words:
            current = root
            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
                current.count += 1  # Increment the count for this prefix
        
        # Step 2: Calculate the prefix scores for each word
        result = []
        
        for word in words:
            current = root
            score = 0
            for char in word:
                current = current.children[char]
                score += current.count  # Add the count of this prefix
            result.append(score)
        
        return result
