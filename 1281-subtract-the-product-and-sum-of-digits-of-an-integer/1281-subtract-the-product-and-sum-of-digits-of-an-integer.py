class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        product = 1
        sum_digits = 0
      
        while n > 0:
            # Extract the last digit using modulus operator
            digit = n % 10
            # Update product and sum
            product *= digit
            sum_digits += digit
            # Remove the last digit from the number
            n //= 10
        
      
        return product - sum_digits


solution = Solution()
print(solution.subtractProductAndSum(234))  # Output: 15
print(solution.subtractProductAndSum(4421)) # Output: 21
