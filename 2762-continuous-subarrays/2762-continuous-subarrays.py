from collections import OrderedDict

class Solution:
    def continuousSubarrays(self, nums):
        n = len(nums)
        count = 0
        i = 0
        j = 0
        ordered_map = OrderedDict()
        
        while j < n:
            # Add the current element to the map
            if nums[j] in ordered_map:
                ordered_map[nums[j]] += 1
            else:
                ordered_map[nums[j]] = 1
            
            # Ensure the difference between max and min keys is <= 2
            while max(ordered_map.keys()) - min(ordered_map.keys()) > 2:
                # Shrink the window from the left
                ordered_map[nums[i]] -= 1
                if ordered_map[nums[i]] == 0:
                    del ordered_map[nums[i]]
                i += 1
            
            # Count valid subarrays ending at index j
            count += j - i + 1
            j += 1
        
        return count
