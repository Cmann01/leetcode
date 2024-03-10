class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        sum_of_digits = 0
        while n > 0:
            sum_of_digits += n % k
            n //= k
        return sum_of_digits

solution = Solution()
print(solution.sumBase(34, 6))  # Output: 9
print(solution.sumBase(10, 10))  # Output: 1
