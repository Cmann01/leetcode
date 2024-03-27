class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
      
        for num in nums:
            # Get the index corresponding to the absolute value of the current number - 1
            index = abs(num) - 1
            # Update the value at the index to be negative if it's positive
            nums[index] = -abs(nums[index])

       
        result = []
        # Iterate through the array again
        for i in range(len(nums)):
            # If the value at index i is positive, it means i+1 is not present in the array
            if nums[i] > 0:
                result.append(i + 1)  # Add i+1 to the result list

       
        return result


solution = Solution()
print(solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))  # Output: [5,6]
print(solution.findDisappearedNumbers([1,1]))              # Output: [2]
