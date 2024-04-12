class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Sort the array
        nums.sort()
        
        # Step 2: Calculate two possibilities
        # Possibility 1: Product of the three largest numbers
        max_prod1 = nums[-1] * nums[-2] * nums[-3]
        # Possibility 2: Product of two smallest (could be negative) and the largest number
        max_prod2 = nums[0] * nums[1] * nums[-1]
        
        # Step 3: Return the maximum of the two possibilities
        return max(max_prod1, max_prod2)
