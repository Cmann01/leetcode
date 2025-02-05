class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # If strings are already equal, return True
        if s1 == s2:
            return True
        
        # Find indices where s1 and s2 differ
        diff = [(i, s1[i], s2[i]) for i in range(len(s1)) if s1[i] != s2[i]]
        
        # There must be exactly two differences, and swapping them should make the strings equal
        return len(diff) == 2 and diff[0][1] == diff[1][2] and diff[0][2] == diff[1][1]
