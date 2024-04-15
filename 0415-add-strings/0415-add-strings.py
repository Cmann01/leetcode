class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        
        
        while i >= 0 or j >= 0 or carry:
            digit_sum = carry
            
            if i >= 0:
                digit_sum += ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                digit_sum += ord(num2[j]) - ord('0')
                j -= 1
            
            
            carry = digit_sum // 10
            digit_sum %= 10
            result.append(str(digit_sum))
        
       
        return ''.join(result[::-1])


solution = Solution()
print(solution.addStrings("11", "123"))  # Output: "134"
print(solution.addStrings("456", "77"))  # Output: "533"
print(solution.addStrings("0", "0"))     # Output: "0"
