from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Helper function to add two fractions
        def addFractions(n1, d1, n2, d2):
            # Find common denominator
            common_denom = d1 * d2
            # Adjust numerators based on the common denominator
            numerator = n1 * d2 + n2 * d1
            # Simplify the fraction
            common_divisor = gcd(abs(numerator), common_denom)
            return numerator // common_divisor, common_denom // common_divisor
        
        # Initialize result fraction as 0/1
        numerator, denominator = 0, 1
        
        # Extract fractions from the expression using regular expression
        i = 0
        length = len(expression)
        
        while i < length:
            # Determine the sign of the fraction
            if expression[i] in '+-':
                sign = 1 if expression[i] == '+' else -1
                i += 1
            else:
                sign = 1
            
            # Extract the numerator
            numerator_start = i
            while expression[i] != '/':
                i += 1
            n = int(expression[numerator_start:i])
            
            # Extract the denominator
            i += 1  # skip '/'
            denominator_start = i
            while i < length and expression[i].isdigit():
                i += 1
            d = int(expression[denominator_start:i])
            
            # Add the current fraction to the result fraction
            numerator, denominator = addFractions(numerator, denominator, sign * n, d)
        
        # If numerator is 0, return 0/1
        if numerator == 0:
            return "0/1"
        
        return f"{numerator}/{denominator}"

# Example usage:
solution = Solution()
print(solution.fractionAddition("-1/2+1/2"))  # Output: "0/1"
print(solution.fractionAddition("-1/2+1/2+1/3"))  # Output: "1/3"
print(solution.fractionAddition("1/3-1/2"))  # Output: "-1/6"
