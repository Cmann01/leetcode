class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()  # Sort the array
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]  # Sum up every alternate element, which are the minimums in pairs
        return result
