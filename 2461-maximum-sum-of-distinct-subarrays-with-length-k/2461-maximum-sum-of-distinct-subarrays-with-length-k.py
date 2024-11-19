from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Initialize variables
        max_sum = 0
        current_sum = 0
        num_count = {}
        
        # Sliding window
        for i in range(len(nums)):
            # Add the current number to the sliding window
            current_sum += nums[i]
            num_count[nums[i]] = num_count.get(nums[i], 0) + 1
            
            # If the window size exceeds k, slide it
            if i >= k:
                left_num = nums[i - k]
                current_sum -= left_num
                num_count[left_num] -= 1
                if num_count[left_num] == 0:
                    del num_count[left_num]
            
            # Check if the current window meets the condition
            if len(num_count) == k:  # All elements are distinct
                max_sum = max(max_sum, current_sum)
        
        return max_sum
