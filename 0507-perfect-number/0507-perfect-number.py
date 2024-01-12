class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False

        # Initialize the sum of divisors
        divisors_sum = 1  # 1 is always a divisor

        # Check divisors up to the square root of num
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                divisors_sum += i
                if i != num // i:  # Avoid counting the same divisor twice
                    divisors_sum += num // i

        # Check if the sum of divisors equals the original number
        return divisors_sum == num

# Example usage:
solution = Solution()
print(solution.checkPerfectNumber(28))  # Output: True
print(solution.checkPerfectNumber(7))   # Output: False
