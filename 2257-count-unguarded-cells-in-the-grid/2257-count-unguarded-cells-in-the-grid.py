class Solution:
    def dfs(self, grid, row, col, rows, cols, direction):
        # Boundary check and skipping guarded or walled cells
        if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 1 or grid[row][col] == 2:
            return

        # Mark the current cell as visited by a guard's line of sight
        grid[row][col] = 3

        # Continue the DFS in the specified direction
        if direction == 1:  # UP
            self.dfs(grid, row - 1, col, rows, cols, direction)
        elif direction == 2:  # DOWN
            self.dfs(grid, row + 1, col, rows, cols, direction)
        elif direction == 3:  # LEFT
            self.dfs(grid, row, col - 1, rows, cols, direction)
        else:  # RIGHT
            self.dfs(grid, row, col + 1, rows, cols, direction)

    def countUnguarded(self, rows, cols, guards, walls):
        # Initialize the grid
        grid = [[0] * cols for _ in range(rows)]

        # Mark guard positions
        for guard in guards:
            i, j = guard
            grid[i][j] = 1  # Guard cell

        # Mark wall positions
        for wall in walls:
            i, j = wall
            grid[i][j] = 2  # Wall cell

        # Perform DFS for each guard in all four directions (UP, DOWN, LEFT, RIGHT)
        for guard in guards:
            guardRow, guardCol = guard
            self.dfs(grid, guardRow - 1, guardCol, rows, cols, 1)  # UP
            self.dfs(grid, guardRow + 1, guardCol, rows, cols, 2)  # DOWN
            self.dfs(grid, guardRow, guardCol - 1, rows, cols, 3)  # LEFT
            self.dfs(grid, guardRow, guardCol + 1, rows, cols, 4)  # RIGHT

        # Count unguarded cells
        unguardedCount = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    unguardedCount += 1

        return unguardedCount
