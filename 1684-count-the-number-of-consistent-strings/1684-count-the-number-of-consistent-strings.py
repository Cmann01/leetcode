class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        # Create a set of allowed characters for O(1) lookup time
        allowed_set = set(allowed)
        count = 0
        
        # Iterate through each word in the words array
        for word in words:
            # Check if all characters in the word are in the allowed set
            if all(char in allowed_set for char in word):
                count += 1
                
        return count
