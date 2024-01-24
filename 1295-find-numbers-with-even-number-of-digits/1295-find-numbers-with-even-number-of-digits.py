class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def count_digits(num):
            """
            Helper function to count the number of digits in a number.
            """
            count = 0
            while num > 0:
                num //= 10
                count += 1
            return count

        # Initialize a variable to store the count of numbers with even digits
        even_digit_count = 0

        # Iterate through the given array
        for num in nums:
            # Check if the number of digits is even
            if count_digits(num) % 2 == 0:
                even_digit_count += 1

        return even_digit_count

# Example usage
solution = Solution()
nums1 = [12, 345, 2, 6, 7896]
print(solution.findNumbers(nums1))  # Output: 2

nums2 = [555, 901, 482, 1771]
print(solution.findNumbers(nums2))  # Output: 1
