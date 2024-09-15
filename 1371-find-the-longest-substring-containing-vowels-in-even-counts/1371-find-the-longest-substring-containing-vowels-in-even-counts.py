class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Map vowels to their respective bit positions in the bitmask
        vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        
        # Initial bitmask and state: state 0 means all vowels are even
        mask = 0
        state_index_map = {0: -1}  # Maps a bitmask to the earliest index it was seen
        max_length = 0
        
        # Traverse the string and update the mask
        for i, char in enumerate(s):
            # If the character is a vowel, flip its corresponding bit
            if char in vowel_to_bit:
                mask ^= (1 << vowel_to_bit[char])
            
            # Check if this state has been seen before
            if mask in state_index_map:
                # Calculate the length of the substring
                max_length = max(max_length, i - state_index_map[mask])
            else:
                # If this is the first time we've seen this mask, store the index
                state_index_map[mask] = i
        
        return max_length
