
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Step 1: Count frequencies of each number
        frequency_map = Counter(nums)
        
        # Step 2: Sort the numbers based on frequency and value
        sorted_nums = sorted(nums, key=lambda x: (frequency_map[x], -x))
        
        return sorted_nums

# Example usage
sol = Solution()
print(sol.frequencySort([1,1,2,2,2,3]))  # Output: [3, 1, 1, 2, 2, 2]
print(sol.frequencySort([2,3,1,3,2]))     # Output: [1, 3, 3, 2, 2]
print(sol.frequencySort([-1,1,-6,4,5,-6,1,4,1]))  # Output: [5, -1, 4, 4, -6, -6, 1, 1, 1]
