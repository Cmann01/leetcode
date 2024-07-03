class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0  # If there are 4 or fewer elements, we can make them all the same
        
        nums.sort()
        
        # Possible minimal differences after at most 3 moves
        return min(
            nums[-1] - nums[3],    # Remove three smallest elements
            nums[-2] - nums[2],    # Remove two smallest and one largest element
            nums[-3] - nums[1],    # Remove one smallest and two largest elements
            nums[-4] - nums[0]     # Remove three largest elements
        )
