class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        result = "1"
        for _ in range(n - 1):
            result = self.getNextSequence(result)
        
        return result
    
    def getNextSequence(self, s):
        result = ""
        i = 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
                i += 1
            result += str(count) + s[i]
            i += 1
        return result
