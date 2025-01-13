class Solution:
    def minimumLength(self, s: str) -> int:
        freq = [0] * 26  # Array to store the frequency of each character
        deleted = 0  # Counter for deleted characters

        for char in s:
            index = ord(char) - ord('a')  # Get the index of the character
            freq[index] += 1

            # If the frequency of the character reaches 3, we remove two characters
            if freq[index] == 3:
                freq[index] -= 2
                deleted += 2

        # The remaining length is the original length minus the number of deleted characters
        return len(s) - deleted
