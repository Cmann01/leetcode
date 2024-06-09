class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Dictionary to store the frequency of prefix sums modulo k
        prefix_count = {0: 1}
        prefix_sum = 0
        count = 0
        
        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            
            # Normalize the mod to be positive
            if mod < 0:
                mod += k
                
            # If this mod has been seen before, there are 'prefix_count[mod]' subarrays
            # ending at the current index with a sum divisible by k.
            if mod in prefix_count:
                count += prefix_count[mod]
                prefix_count[mod] += 1
            else:
                prefix_count[mod] = 1
        
        return count

# Example usage:
sol = Solution()
print(sol.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))  # Output: 7
print(sol.subarraysDivByK([5], 9))  # Output: 0
