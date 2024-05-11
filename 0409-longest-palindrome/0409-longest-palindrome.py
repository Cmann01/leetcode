class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Count the frequency of each character
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Initialize the length of the longest palindrome
        longest_length = 0

        # Flag to indicate if there is a character with an odd count
        odd_flag = False

        # Iterate through the character counts
        for count in char_count.values():
            if count % 2 == 0:
                # If count is even, add it to the palindrome length
                longest_length += count
            else:
                # If count is odd, add count - 1 to the palindrome length
                longest_length += count - 1
                # Set the flag to True indicating there's an odd count character
                odd_flag = True

        # If there's at least one character with an odd count, add one to the length
        if odd_flag:
            longest_length += 1

        return longest_length
