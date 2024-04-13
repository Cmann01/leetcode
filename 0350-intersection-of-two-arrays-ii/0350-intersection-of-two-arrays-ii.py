class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
       
        num_counts = {}
       
        for num in nums1:
            num_counts[num] = num_counts.get(num, 0) + 1
        
        intersection = []
        
        for num in nums2:
            if num in num_counts and num_counts[num] > 0:
                intersection.append(num)
                num_counts[num] -= 1
        return intersection
