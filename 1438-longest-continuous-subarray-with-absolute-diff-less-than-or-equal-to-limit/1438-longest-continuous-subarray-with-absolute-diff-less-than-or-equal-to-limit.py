from collections import deque

class Solution:
    def longestSubarray(self, nums, limit):
        min_deque = deque()
        max_deque = deque()
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            # Maintain the min_deque for the current window
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # Maintain the max_deque for the current window
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # Check the current window validity
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                # Remove elements from deques that are out of the current window
                if min_deque[0] < left:
                    min_deque.popleft()
                if max_deque[0] < left:
                    max_deque.popleft()
                    
            # Update the maximum length of valid subarray
            max_length = max(max_length, right - left + 1)
        
        return max_length
