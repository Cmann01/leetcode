class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                # Pop characters until we find an opening parenthesis
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                # Pop the opening parenthesis
                stack.pop()
                # Push the reversed substring back onto the stack
                stack.extend(temp)
            else:
                # Push the current character onto the stack
                stack.append(char)
        
        # Join the characters to form the final string
        return ''.join(stack)

# Example usage:
solution = Solution()
print(solution.reverseParentheses("(abcd)"))  # Output: "dcba"
print(solution.reverseParentheses("(u(love)i)"))  # Output: "iloveu"
print(solution.reverseParentheses("(ed(et(oc))el)"))  # Output: "leetcode"
