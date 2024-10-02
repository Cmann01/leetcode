class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Step 1: Create a sorted list of unique elements from arr
        sorted_unique = sorted(set(arr))
        
        # Step 2: Create a mapping from each element to its rank
        rank_map = {value: rank + 1 for rank, value in enumerate(sorted_unique)}
        
        # Step 3: Replace each element in the original array with its rank
        return [rank_map[num] for num in arr]
