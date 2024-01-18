class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize the result to store the XOR of all elements
        result = 0
        
        # XOR all elements in the array
        for num in nums:
            result ^= num
        
        return result