from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Count the frequencies of each element in both arrays
        counts1 = Counter(nums1)
        counts2 = Counter(nums2)
        
        # Find the intersection of both counts
        intersection = counts1 & counts2
        
        # Construct the result array based on the intersection counts
        result = []
        for num in intersection:
            result.extend([num] * intersection[num])
        
        return result
