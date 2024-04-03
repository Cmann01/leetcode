class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        ranges = []
        start = nums[0]
        end = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append(str(start) + "->" + str(end))
                start = nums[i]
                end = nums[i]
        
        if start == end:
            ranges.append(str(start))
        else:
            ranges.append(str(start) + "->" + str(end))
        
        return ranges

nums1 = [0, 1, 2, 4, 5, 7]
solution = Solution()
print(solution.summaryRanges(nums1))  # Output: ["0->2", "4->5", "7"]

nums2 = [0, 2, 3, 4, 6, 8, 9]
print(solution.summaryRanges(nums2))  # Output: ["0", "2->4", "6", "8->9"]
