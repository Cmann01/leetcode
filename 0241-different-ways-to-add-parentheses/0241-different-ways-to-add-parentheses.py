class Solution:
    def diffWaysToCompute(self, expression: str):
        # If the expression is a number, return it as a list containing that number
        if expression.isdigit():
            return [int(expression)]
        
        result = []
        
        # Iterate through the expression
        for i, char in enumerate(expression):
            # If the current character is an operator, split the expression
            if char in '+-*':
                # Recursively solve for the left and right sides of the operator
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                
                # Combine the results from left and right sub-expressions
                for l in left:
                    for r in right:
                        if char == '+':
                            result.append(l + r)
                        elif char == '-':
                            result.append(l - r)
                        elif char == '*':
                            result.append(l * r)
        
        return result
