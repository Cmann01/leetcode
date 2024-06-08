class Solution:
    def checkSubarraySum(self, nums, k):
        # Dictionary to store (modulus, index)
        mod_dict = {0: -1}  # Initialize with 0:-1 to handle subarrays starting from index 0
        prefix_sum = 0
        
        for i, num in enumerate(nums):
            prefix_sum += num
            mod = prefix_sum % k
            
            if mod in mod_dict:
                if i - mod_dict[mod] > 1:
                    return True
            else:
                mod_dict[mod] = i
        
        return False
