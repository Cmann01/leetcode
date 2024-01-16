class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Check if the length of the set of nums is different from the length of nums
        # If they are different, it means there are duplicates
        return len(set(nums)) != len(nums)

# Example usage:
solution = Solution()

nums1 = [1, 2, 3, 1]
print(solution.containsDuplicate(nums1))  # Output: True

nums2 = [1, 2, 3, 4]
print(solution.containsDuplicate(nums2))  # Output: False

nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(solution.containsDuplicate(nums3))  # Output: True
