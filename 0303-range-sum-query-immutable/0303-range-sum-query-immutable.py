class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.cumulative_sum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.cumulative_sum[i] = self.cumulative_sum[i - 1] + nums[i - 1]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.cumulative_sum[right + 1] - self.cumulative_sum[left]

# Example usage:
numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))  # Output: 1
print(numArray.sumRange(2, 5))  # Output: -1
print(numArray.sumRange(0, 5))  # Output: -3
