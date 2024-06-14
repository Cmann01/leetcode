class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort the array
        nums.sort()
        
        # This will hold the total number of moves needed
        moves = 0
        
        # Iterate through the array and adjust elements to make them unique
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:  # If current element is not greater than the previous
                increment = nums[i - 1] - nums[i] + 1
                nums[i] += increment  # Increment the current element
                moves += increment  # Add the number of increments to the total moves
        
        return moves

# Example usage
solution = Solution()
print(solution.minIncrementForUnique([1, 2, 2]))  # Output: 1
print(solution.minIncrementForUnique([3, 2, 1, 2, 1, 7]))  # Output: 6
