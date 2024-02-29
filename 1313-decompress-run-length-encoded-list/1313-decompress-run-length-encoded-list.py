class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        decompressed_list = []
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i + 1]
            decompressed_list.extend([val] * freq)
        return decompressed_list
