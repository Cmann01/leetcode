from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(counter):
            nonlocal count
            for char in counter:
                if counter[char] > 0:
                    # Choose this character
                    count += 1
                    counter[char] -= 1

                    # Recursively backtrack
                    backtrack(counter)

                    # Undo the choice (backtrack)
                    counter[char] += 1

        count = 0
        counter = Counter(tiles)
        backtrack(counter)
        return count
