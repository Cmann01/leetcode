class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Split the string into words
        words = s.split()

        # Sort the words based on the last character (which is a digit)
        words.sort(key=lambda x: int(x[-1]))

        # Extract the original words by removing the last character from each word
        original_words = [word[:-1] for word in words]

        # Join the words into a sentence
        original_sentence = ' '.join(original_words)

        return original_sentence

# Example usage:
solution = Solution()
s1 = "is2 sentence4 This1 a3"
print(solution.sortSentence(s1))  # Output: "This is a sentence"

s2 = "Myself2 Me1 I4 and3"
print(solution.sortSentence(s2))  # Output: "Me Myself and I"
