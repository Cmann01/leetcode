class Solution:
    def minLength(self, s: str) -> int:
        # Stack to process the string
        stack = []
        
        # Loop through each character in the string
        for char in s:
            # Check for "AB" or "CD" as top two elements in stack
            if stack and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D')):
                # Remove the last character (part of "AB" or "CD")
                stack.pop()
            else:
                # Otherwise, add current character to stack
                stack.append(char)
        
        # The remaining length of the stack is the minimum possible length of the resulting string
        return len(stack)
