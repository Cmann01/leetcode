from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0
        
        for j in range(n):
            left_less = left_more = 0
            right_less = right_more = 0
            
            # Count the number of valid ratings on the left and right of `j`
            for i in range(j):
                if rating[i] < rating[j]:
                    left_less += 1
                else:
                    left_more += 1
            
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_less += 1
                else:
                    right_more += 1
            
            # Count teams: (i < j < k) where rating[i] < rating[j] < rating[k]
            count += left_less * right_more  # increasing sequence
            # Count teams: (i < j < k) where rating[i] > rating[j] > rating[k]
            count += left_more * right_less  # decreasing sequence
        
        return count
