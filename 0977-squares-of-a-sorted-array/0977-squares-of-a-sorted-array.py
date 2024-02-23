class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Initialize an array to store the squared values
        squares = [0] * len(nums)
        
        # Pointers for the leftmost and rightmost elements in the original array
        left, right = 0, len(nums) - 1
        
        # Pointer for the rightmost position in the squares array
        index = len(nums) - 1
        
        # Loop until left pointer crosses the right pointer
        while left <= right:
            # Square the numbers and compare
            if abs(nums[left]) > abs(nums[right]):
                squares[index] = nums[left] * nums[left]
                left += 1
            else:
                squares[index] = nums[right] * nums[right]
                right -= 1
            # Move one step towards the left in the squares array
            index -= 1
        
        return squares