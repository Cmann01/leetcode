class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        
        for char in expression:
            if char == ',':
                # Ignore commas, they are just separators in the input
                continue
            elif char in 'tf':  # Push 't' or 'f' directly to stack
                stack.append(char)
            elif char == ')':  # Time to evaluate a sub-expression
                sub_expr = []
                while stack[-1] != '(':  # Get everything inside the parenthesis
                    sub_expr.append(stack.pop())
                stack.pop()  # Remove '('

                operator = stack.pop()  # The operator before '('
                if operator == '&':
                    # AND operation: Result is true if all are true
                    result = all(val == 't' for val in sub_expr)
                elif operator == '|':
                    # OR operation: Result is true if at least one is true
                    result = any(val == 't' for val in sub_expr)
                elif operator == '!':
                    # NOT operation: Negate the single sub-expression
                    result = sub_expr[0] == 'f'

                # Push the result of the evaluated sub-expression back to the stack
                stack.append('t' if result else 'f')
            else:
                # It's one of '(', '&', '|', or '!', just push to the stack
                stack.append(char)
        
        # The final result will be the last element in the stack
        return stack[-1] == 't'

# Example usage
solution = Solution()
print(solution.parseBoolExpr("&(|(f))"))  # Output: False
print(solution.parseBoolExpr("|(f,f,f,t)"))  # Output: True
print(solution.parseBoolExpr("!(&(f,t))"))  # Output: True
