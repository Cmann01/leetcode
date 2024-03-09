class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        lines = 1
        width = 0
        
        for char in s:
            char_width = widths[ord(char) - ord('a')]
            width += char_width
            if width > 100:
                lines += 1
                width = char_width
        
        return [lines, width]
