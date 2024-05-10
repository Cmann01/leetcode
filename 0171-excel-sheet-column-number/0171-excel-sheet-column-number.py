class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        column_number = 0
        for char in columnTitle:
            column_number = column_number * 26 + (ord(char) - ord('A') + 1)
        return column_number

# Example usage:
solution = Solution()
print(solution.titleToNumber("A"))    # Output: 1
print(solution.titleToNumber("AB"))   # Output: 28
print(solution.titleToNumber("ZY"))   # Output: 701
