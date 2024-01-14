class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_next_number(num):
            # Helper function to calculate the sum of squares of digits
            result = 0
            while num > 0:
                digit = num % 10
                result += digit ** 2
                num //= 10
            return result
        
        # Use a set to detect cycles
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next_number(n)
        
        return n == 1
