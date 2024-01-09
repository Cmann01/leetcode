class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Check if the array is empty
        if not nums:
            return 0

        # Initialize the unique element count
        k = 1

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the previous one,
            # update the array and increment the unique element count
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        # The first k elements of nums now contain the unique elements
        # The remaining elements of nums are not important

        return k

# Example usage:
nums1 = [1, 1, 2]
expectedNums1 = [1, 2]
solution1 = Solution()
k1 = solution1.removeDuplicates(nums1)
assert k1 == len(expectedNums1)
for i in range(k1):
    assert nums1[i] == expectedNums1[i]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
expectedNums2 = [0, 1, 2, 3, 4]
solution2 = Solution()
k2 = solution2.removeDuplicates(nums2)
assert k2 == len(expectedNums2)
for i in range(k2):
    assert nums2[i] == expectedNums2[i]
    
    
    
    
