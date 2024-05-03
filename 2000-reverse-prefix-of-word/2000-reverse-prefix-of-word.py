class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        index = word.find(ch)  # Find the index of the first occurrence of ch
        if index != -1:  # If ch exists in word
            return word[:index+1][::-1] + word[index+1:]  # Reverse the substring from 0 to index and concatenate with the rest of word
        else:
            return word  # Return word unchanged if ch doesn't exist in it
