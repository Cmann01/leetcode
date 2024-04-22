class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
      
        sorted_chars = sorted(char_count.keys(), key=lambda x: char_count[x], reverse=True)
        
        
        sorted_string = ""
        for char in sorted_chars:
            sorted_string += char * char_count[char]
        
        return sorted_string
