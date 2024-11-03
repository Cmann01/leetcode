class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if lengths are the same, otherwise they can't be rotations
        if len(s) != len(goal):
            return False
        # Check if goal is a substring of s + s
        return goal in (s + s)
