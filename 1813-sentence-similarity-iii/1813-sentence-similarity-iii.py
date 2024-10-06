class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Split the sentences into words
        words1 = sentence1.split()
        words2 = sentence2.split()

        # Get lengths of both sentences
        n1, n2 = len(words1), len(words2)

        # Ensure words1 is the longer one
        if n1 < n2:
            words1, words2 = words2, words1
            n1, n2 = n2, n1

        # Compare from the start and the end
        start, end = 0, 0

        # Match words from the start
        while start < n2 and words1[start] == words2[start]:
            start += 1

        # Match words from the end
        while end < n2 - start and words1[-(end + 1)] == words2[-(end + 1)]:
            end += 1

        # If the entire sentence2 is matched, return True
        return start + end >= n2
