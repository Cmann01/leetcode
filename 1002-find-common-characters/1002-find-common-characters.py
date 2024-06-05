class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return []

        # Initialize the frequency dictionary with the first word
        freq = {char: words[0].count(char) for char in words[0]}

        # Update the frequency dictionary based on each subsequent word
        for word in words[1:]:
            current_freq = {char: word.count(char) for char in word}
            for char in freq:
                if char in current_freq:
                    freq[char] = min(freq[char], current_freq[char])
                else:
                    freq[char] = 0

        # Build the result list based on the frequency dictionary
        result = []
        for char, count in freq.items():
            result.extend([char] * count)

        return result
