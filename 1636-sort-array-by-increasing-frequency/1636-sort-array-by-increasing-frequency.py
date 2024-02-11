class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Count the frequency of each number
        count = collections.Counter(nums)

        # Sort the numbers based on their frequency and values
        nums.sort(key=lambda x: (count[x], -x))

        return nums
