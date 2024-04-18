class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_max = second_max = third_max = float('-inf')

        for num in nums:
            if num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif num > second_max and num != first_max:
                third_max = second_max
                second_max = num
            elif num > third_max and num != first_max and num != second_max:
                third_max = num

        if third_max != float('-inf'):
            return third_max
        else:
            return first_max

# Example usage:
# nums = [3, 2, 1]
# solution = Solution()
# print(solution.thirdMax(nums))
