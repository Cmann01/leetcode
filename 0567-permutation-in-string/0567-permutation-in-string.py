class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        
        len_s1, len_s2 = len(s1), len(s2)
        
        # If s1 is longer than s2, s2 can't contain a permutation of s1
        if len_s1 > len_s2:
            return False
        
        # Create a counter for the frequency of characters in s1
        s1_count = Counter(s1)
        # Create a counter for the first window in s2 of size len(s1)
        window_count = Counter(s2[:len_s1])
        
        # If the first window matches, return True
        if s1_count == window_count:
            return True
        
        # Now slide the window across s2
        for i in range(len_s1, len_s2):
            # Remove the character going out of the window
            window_count[s2[i - len_s1]] -= 1
            if window_count[s2[i - len_s1]] == 0:
                del window_count[s2[i - len_s1]]
            
            # Add the new character to the window
            window_count[s2[i]] += 1
            
            # Check if the window matches s1's frequency count
            if window_count == s1_count:
                return True
        
        # No permutation found
        return False
