from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # Dimensions of the matrix
        m, n = len(mat), len(mat[0])
        
        # Map each value in the matrix to its row and column
        value_to_index = {}
        for r in range(m):
            for c in range(n):
                value_to_index[mat[r][c]] = (r, c)
        
        # Track the count of painted cells in each row and column
        row_paint = [0] * m
        col_paint = [0] * n
        
        # Process the array
        for i, val in enumerate(arr):
            # Find the corresponding row and column for the current value
            r, c = value_to_index[val]
            
            # Paint the cell
            row_paint[r] += 1
            col_paint[c] += 1
            
            # Check if any row or column is fully painted
            if row_paint[r] == n or col_paint[c] == m:
                return i
        
        return -1  # Should never reach here as per problem constraints
