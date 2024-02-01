class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Count the occurrences of each character
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        
        result = ""
        
        while len(result) < len(s):
            # Append characters in increasing order
            for i in range(26):
                if count[i] > 0:
                    result += chr(ord('a') + i)
                    count[i] -= 1
            
            # Append characters in decreasing order
            for i in range(25, -1, -1):
                if count[i] > 0:
                    result += chr(ord('a') + i)
                    count[i] -= 1
        
        return result
