class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        xor_result = 0
        for char in s:
            xor_result ^= ord(char)
        for char in t:
            xor_result ^= ord(char)
        return chr(xor_result)
