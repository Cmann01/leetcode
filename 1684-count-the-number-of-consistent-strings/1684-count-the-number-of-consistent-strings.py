class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        # Create a set to store allowed characters for O(1) lookup
        allowed_set = set(allowed)
        
        # Initialize a counter for consistent strings
        consistent_count = 0
        
        # Iterate through each word in the list of words
        for word in words:
            # Assume the word is consistent initially
            is_consistent = True
            # Check each character in the word
            for char in word:
                # If any character in the word is not in the allowed set,
                # mark the word as inconsistent and break the loop
                if char not in allowed_set:
                    is_consistent = False
                    break
            # If the word is consistent, increment the count
            if is_consistent:
                consistent_count += 1
        
        # Return the count of consistent strings
        return consistent_count
