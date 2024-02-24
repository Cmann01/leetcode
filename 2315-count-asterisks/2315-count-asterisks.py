class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        is_between_bars = False

        for char in s:
            if char == '|':
                is_between_bars = not is_between_bars
            elif char == '*' and not is_between_bars:
                count += 1

        return count

# Test cases
solution = Solution()
print(solution.countAsterisks("l|*e*et|c**o|*de|"))  # Output: 2
print(solution.countAsterisks("iamprogrammer"))        # Output: 0
print(solution.countAsterisks("yo|uar|e**|b|e***au|tifu|l"))  # Output: 5
