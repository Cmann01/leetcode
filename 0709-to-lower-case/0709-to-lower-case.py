class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s.lower()

# Test cases
solution = Solution()
print(solution.toLowerCase("Hello"))  # Output: "hello"
print(solution.toLowerCase("here"))   # Output: "here"
print(solution.toLowerCase("LOVELY")) # Output: "lovely"
