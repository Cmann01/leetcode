class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        # Use binary search to find the square root
        left, right = 1, x
        result = 0

        while left <= right:
            mid = (left + right) // 2

            # Check if mid is the square root
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result

# Example usage:
solution = Solution()
print(solution.mySqrt(4))  # Output: 2
print(solution.mySqrt(8))  # Output: 2
