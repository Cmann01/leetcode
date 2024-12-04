class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0  # Pointers for str1 and str2
        
        while i < len(str1) and j < len(str2):
            # Current character and its cyclic increment
            current_char = str1[i]
            next_char = chr(((ord(current_char) - ord('a') + 1) % 26) + ord('a'))
            
            # Check if we can match str2[j] with str1[i] or its cyclic increment
            if str2[j] == current_char or str2[j] == next_char:
                j += 1  # Move pointer for str2 if a match is found
            
            i += 1  # Always move pointer for str1
        
        # If we've matched all characters of str2, return True
        return j == len(str2)
