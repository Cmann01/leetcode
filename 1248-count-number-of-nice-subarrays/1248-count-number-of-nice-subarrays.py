from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums, k):
        count = 0
        prefix_sums = defaultdict(int)
        prefix_sum = 0
        
        # Initialize with 0 prefix sum to handle subarrays starting from index 0
        prefix_sums[0] = 1
        
        for num in nums:
            # Increment prefix sum if the current number is odd
            prefix_sum += num % 2
            
            # If there's a prefix sum that equals current prefix_sum - k, it means we found a valid subarray
            if prefix_sum - k in prefix_sums:
                count += prefix_sums[prefix_sum - k]
            
            # Update the prefix sums hash map
            prefix_sums[prefix_sum] += 1
        
        return count
