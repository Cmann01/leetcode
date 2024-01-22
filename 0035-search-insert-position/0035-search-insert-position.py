class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        # If the target is not found, low represents the index where it should be inserted.
        return low

# Example usage:
# Create a Solution object and test the searchInsert function.
sol = Solution()

nums1, target1 = [1, 3, 5, 6], 5
nums2, target2 = [1, 3, 5, 6], 2
nums3, target3 = [1, 3, 5, 6], 7

print(sol.searchInsert(nums1, target1))  # Output: 2
print(sol.searchInsert(nums2, target2))  # Output: 1
print(sol.searchInsert(nums3, target3))  # Output: 4
