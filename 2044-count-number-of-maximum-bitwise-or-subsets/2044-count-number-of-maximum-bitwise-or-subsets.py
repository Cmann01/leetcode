from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Step 1: Find the maximum bitwise OR value
        max_or = 0
        for num in nums:
            max_or |= num  # OR-ing all elements to get the maximum possible OR
        
        # Step 2: Initialize the counter for subsets that match max_or
        count = 0
        
        # Step 3: Generate all possible subsets and check their OR values
        def backtrack(i, current_or):
            nonlocal count
            if i == len(nums):
                if current_or == max_or:
                    count += 1
                return
            
            # Include nums[i] in the subset
            backtrack(i + 1, current_or | nums[i])
            
            # Exclude nums[i] from the subset
            backtrack(i + 1, current_or)
        
        # Start the backtracking process from index 0 with initial OR value 0
        backtrack(0, 0)
        
        return count
