class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0
        
        while i < len(word):
            # Current character
            c = word[i]
            # Calculate the maximum prefix of the same character 'c' (up to 9 times)
            count = 0
            while i < len(word) and word[i] == c and count < 9:
                i += 1
                count += 1
            # Append count and character to the result
            comp += str(count) + c
        
        return comp
