class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # Initialize the result
        result = 0
        
        # Iterate through the string from left to right
        for i in range(len(s)):
            # If the current symbol is smaller than the next symbol, subtract its value
            if i < len(s) - 1 and roman_dict[s[i]] < roman_dict[s[i+1]]:
                result -= roman_dict[s[i]]
            else:
                # Otherwise, add its value
                result += roman_dict[s[i]]
        
        return result

# Test cases
sol = Solution()
print(sol.romanToInt("III"))      # Output: 3
print(sol.romanToInt("LVIII"))    # Output: 58
print(sol.romanToInt("MCMXCIV"))  # Output: 1994
