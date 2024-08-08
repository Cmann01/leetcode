class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int):
        # Define the directions for the movement: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # The initial position and step sizes
        x, y = rStart, cStart
        step = 1
        result = [[x, y]]
        total_cells = rows * cols
        dir_index = 0  # Start with moving right

        while len(result) < total_cells:
            for _ in range(2):  # We need to move in the current direction twice (before changing direction)
                for _ in range(step):
                    x += directions[dir_index][0]
                    y += directions[dir_index][1]
                    if 0 <= x < rows and 0 <= y < cols:
                        result.append([x, y])
                dir_index = (dir_index + 1) % 4  # Change direction clockwise
            step += 1  # Increase step size after completing a full circle

        return result
