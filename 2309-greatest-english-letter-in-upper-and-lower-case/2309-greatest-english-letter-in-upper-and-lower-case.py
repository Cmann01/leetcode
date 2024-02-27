class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Create a set to store unique characters
        letters = set()

        # Iterate through the string to find unique characters
        for char in s:
            # Add the character to the set if it's an uppercase letter
            if char.isupper():
                letters.add(char)

        result = ''

        # Iterate through the alphabet in reverse order
        for char in reversed('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            # Check if the character exists in both uppercase and lowercase
            if char in letters and char.lower() in s:
                result = char
                break

        return result

# Example usage:
solution = Solution()
print(solution.greatestLetter("lEeTcOdE"))  # Output: "E"
print(solution.greatestLetter("arRAzFif"))   # Output: "R"
print(solution.greatestLetter("AbCdEfGhIjK"))# Output: ""
