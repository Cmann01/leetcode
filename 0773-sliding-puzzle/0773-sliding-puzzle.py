from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def neighbors(board):
            zero_row, zero_col = next((i, j) for i in range(2) for j in range(3) if board[i][j] == 0)
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = zero_row + dr, zero_col + dc
                if 0 <= new_row < 2 and 0 <= new_col < 3:
                    new_board = [list(row) for row in board]  # Convert to list for modification
                    new_board[zero_row][zero_col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[zero_row][zero_col]
                    yield tuple(map(tuple, new_board))  # Convert back to tuple

        queue = deque([(tuple(map(tuple, board)), 0)])
        visited = set()
        target = ((1, 2, 3), (4, 5, 0))

        while queue:
            board, moves = queue.popleft()
            if board == target:
                return moves
            if board in visited:
                continue
            visited.add(board)
            for neighbor in neighbors(board):
                queue.append((neighbor, moves + 1))

        return -1