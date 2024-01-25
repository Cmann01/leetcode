class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        # Split the text into words
        words = text.split()

        # Convert brokenLetters into a set for faster lookup
        broken_set = set(brokenLetters)

        # Initialize a count for words that can be typed
        count = 0

        # Iterate through each word in the text
        for word in words:
            # Flag to indicate if the word can be typed
            can_type = True
            # Check each letter in the word
            for letter in word:
                # If the letter is in brokenLetters, mark the word as unable to be typed
                if letter in broken_set:
                    can_type = False
                    break  # No need to check further if one letter is broken
            # If the word can be typed, increment the count
            if can_type:
                count += 1

        return count
