class Solution:
    def minChanges(self, s: str) -> int:
        curr = s[0]
        count = 0
        changes = 0
        n = len(s)

        for i in range(n):
            if s[i] == curr:
                count += 1
                continue

            # Check if the count of the current character is even
            if count % 2 == 0:
                count = 1
            else:
                count = 0
                changes += 1

            curr = s[i]

        return changes
