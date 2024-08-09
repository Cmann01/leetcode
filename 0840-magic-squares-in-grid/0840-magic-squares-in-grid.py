class Solution:
    def isMagic(self, grid: List[List[int]], r: int, c: int) -> bool:
        s = set()
        # Check all values are distinct and within 1 to 9
        for i in range(3):
            for j in range(3):
                num = grid[r+i][c+j]
                if num < 1 or num > 9 or num in s:
                    return False
                s.add(num)
        
        # Check rows, columns and diagonals sums
        return (grid[r][c] + grid[r][c+1] + grid[r][c+2] == 
                grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == 
                grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] ==
                grid[r][c] + grid[r+1][c] + grid[r+2][c] == 
                grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 
                grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] ==
                grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] ==
                grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c])
    
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        
        count = 0
        for r in range(len(grid) - 2):
            for c in range(len(grid[0]) - 2):
                if grid[r+1][c+1] == 5 and self.isMagic(grid, r, c):
                    count += 1
                    
        return count
