from typing import List
from collections import defaultdict

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # Group numbers by their set-bit count
        bit_count_groups = defaultdict(list)
        
        for num in nums:
            bit_count = bin(num).count('1')
            bit_count_groups[bit_count].append(num)
        
        # Sort each group independently
        sorted_nums = []
        
        for bit_count in sorted(bit_count_groups.keys()):
            sorted_nums.extend(sorted(bit_count_groups[bit_count]))
        
        # Check if sorted result matches the sorted input array
        return sorted_nums == sorted(nums)
