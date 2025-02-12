from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Helper function to calculate sum of digits
        def sum_of_digits(n: int) -> int:
            return sum(int(digit) for digit in str(n))
        
        # Dictionary to group numbers by sum of digits
        digit_sum_groups = {}
        
        # Group numbers by their sum of digits
        for num in nums:
            digit_sum = sum_of_digits(num)
            if digit_sum not in digit_sum_groups:
                digit_sum_groups[digit_sum] = []
            digit_sum_groups[digit_sum].append(num)
        
        # Find the maximum sum of any two numbers in the same group
        max_sum = -1
        for group in digit_sum_groups.values():
            if len(group) > 1:
                # Sort the group in descending order
                group.sort(reverse=True)
                # Calculate the sum of the two largest numbers
                max_sum = max(max_sum, group[0] + group[1])
        
        return max_sum

# Example usage
solution = Solution()
print(solution.maximumSum([18, 43, 36, 13, 7]))  # Output: 54
print(solution.maximumSum([10, 12, 19, 14]))     # Output: -1
