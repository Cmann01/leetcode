class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for char in s:
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:
                stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)

# Example usage:
solution = Solution()
print(solution.makeGood("leEeetcode"))  # Output: "leetcode"
print(solution.makeGood("abBAcC"))      # Output: ""
print(solution.makeGood("s"))           # Output: "s"
