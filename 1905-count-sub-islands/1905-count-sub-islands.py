class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(r, c):
            # If out of bounds or water in grid2, return True (base case)
            if r < 0 or r >= len(grid2) or c < 0 or c >= len(grid2[0]) or grid2[r][c] == 0:
                return True
            
            # Mark the cell as visited in grid2
            grid2[r][c] = 0
            
            # If this part of the island is not in grid1, it's not a sub-island
            is_sub_island = grid1[r][c] == 1
            
            # Check all 4 directions (up, down, left, right)
            is_sub_island = dfs(r + 1, c) and is_sub_island
            is_sub_island = dfs(r - 1, c) and is_sub_island
            is_sub_island = dfs(r, c + 1) and is_sub_island
            is_sub_island = dfs(r, c - 1) and is_sub_island
            
            return is_sub_island
        
        # Initialize the count of sub-islands
        count = 0
        
        # Iterate through every cell in grid2
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                # If we find a part of an island in grid2
                if grid2[r][c] == 1:
                    # If the island in grid2 is a sub-island, increment the count
                    if dfs(r, c):
                        count += 1
        
        return count
