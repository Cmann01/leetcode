class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1

# Example usage:
solution = Solution()
print(solution.strStr("sadbutsad", "sad"))  # Output: 0
print(solution.strStr("leetcode", "leeto"))  # Output: -1
