class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        
        s_count = [0] * 26
        for char in s:
            s_count[ord(char) - ord('a')] += 1
        
        
        for char in t:
            index = ord(char) - ord('a')
            s_count[index] -= 1
            if s_count[index] < 0:
                return False
        
        
        return all(count == 0 for count in s_count)
