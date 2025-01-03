class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        # Calculate the total sum of the array
        total_sum = sum(nums)
        
        # Initialize the prefix sum and the count of valid splits
        prefix_sum = 0
        valid_splits = 0
        
        # Iterate through the array up to the second last element
        for i in range(len(nums) - 1):
            # Update the prefix sum
            prefix_sum += nums[i]
            
            # Calculate the sum of the right part
            right_sum = total_sum - prefix_sum
            
            # Check if the current split is valid
            if prefix_sum >= right_sum:
                valid_splits += 1
        
        return valid_splits
