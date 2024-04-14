class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        
        if len(s) != len(goal) or not s or not goal:
            return False
        
        
        if s == goal:
            seen = set()
            for char in s:
                if char in seen:
                    return True
                seen.add(char)
            return False
        
       
        diffs = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diffs.append(i)
                
        
        if len(diffs) != 2:
            return False
        
        
        return s[diffs[0]] == goal[diffs[1]] and s[diffs[1]] == goal[diffs[0]]

# Example usage
solution = Solution()
print(solution.buddyStrings("ab", "ba"))  # Output: true
print(solution.buddyStrings("ab", "ab"))  # Output: false
print(solution.buddyStrings("aa", "aa"))  # Output: true
