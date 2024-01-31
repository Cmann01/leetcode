class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # Initialize a list to store the minimum frequency of characters
        min_freq = [float('inf')] * 26  # There are 26 lowercase English letters

        # Iterate through each word
        for word in words:
            # Initialize a frequency list for the current word
            freq = [0] * 26

            # Count the frequency of characters in the current word
            for char in word:
                freq[ord(char) - ord('a')] += 1

            # Update the minimum frequency list
            for i in range(26):
                min_freq[i] = min(min_freq[i], freq[i])

        # Initialize the result list to store common characters
        result = []

        # Generate the common characters based on the minimum frequency
        for i in range(26):
            if min_freq[i] > 0:
                result.extend([chr(i + ord('a'))] * min_freq[i])

        return result

# Test cases
solution = Solution()
print(solution.commonChars(["bella", "label", "roller"]))  # Output: ["e", "l", "l"]
print(solution.commonChars(["cool", "lock", "cook"]))      # Output: ["c", "o"]
