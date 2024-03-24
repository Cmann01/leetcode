class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Split the string into words
        words = s.split()
        
        # Reverse each word and join them back
        reversed_words = [word[::-1] for word in words]
        
        # Join the reversed words with space
        return ' '.join(reversed_words)
