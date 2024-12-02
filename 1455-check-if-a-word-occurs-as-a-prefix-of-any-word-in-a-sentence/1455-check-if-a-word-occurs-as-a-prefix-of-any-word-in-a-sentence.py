class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # Split the sentence into words
        words = sentence.split()
        
        # Iterate through the words with their indices
        for index, word in enumerate(words):
            # Check if searchWord is a prefix of the current word
            if word.startswith(searchWord):
                # Return the 1-based index
                return index + 1
        
        # If no word matches, return -1
        return -1
