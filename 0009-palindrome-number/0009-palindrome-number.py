class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Handle negative numbers and numbers ending with 0 (excluding 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Initialize reversed number
        reversed_num = 0

        # Reverse the second half of the number
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        # For even-length palindrome, x and reversed_num will be equal
        # For odd-length palindrome, x will be one digit shorter than reversed_num
        return x == reversed_num or x == reversed_num // 10
