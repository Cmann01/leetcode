class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        j = 0  # Pointer for string t
        
        # Traverse through string s
        for i in range(m):
            if j < n and s[i] == t[j]:
                j += 1
        
        # If j characters of t are already a subsequence of s,
        # we need to append the rest (n - j) characters
        return n - j
