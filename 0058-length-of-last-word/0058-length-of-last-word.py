class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Split the string into words using spaces as separators
        words = s.split()

        # Check if there are any words in the string
        if not words:
            return 0

        # Return the length of the last word
        return len(words[-1])

solution = Solution()
print(solution.lengthOfLastWord("Hello World"))  # Output: 5
print(solution.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print(solution.lengthOfLastWord("luffy is still joyboy"))  # Output: 6
