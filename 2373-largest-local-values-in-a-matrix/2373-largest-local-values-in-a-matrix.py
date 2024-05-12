class Solution(object):
    def largestLocal(self, grid):
        n = len(grid)
        result = []
        for i in range(1, n - 1):
            row = []
            for j in range(1, n - 1):
                submatrix = [grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],
                             grid[i][j-1],   grid[i][j],   grid[i][j+1],
                             grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]]
                row.append(max(submatrix))
            result.append(row)
        return result

# Example usage:
grid1 = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
solution = Solution()
print(solution.largestLocal(grid1))  # Output: [[9, 9], [8, 6]]

grid2 = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
print(solution.largestLocal(grid2))  # Output: [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
