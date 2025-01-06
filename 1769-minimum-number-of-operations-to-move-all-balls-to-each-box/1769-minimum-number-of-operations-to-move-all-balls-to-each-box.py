class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        answer = [0] * n
        
        # Pass 1: From left to right
        count = 0  # Count of balls to the left
        operations = 0  # Total operations to the left
        for i in range(n):
            answer[i] += operations
            count += int(boxes[i])
            operations += count
        
        # Pass 2: From right to left
        count = 0  # Count of balls to the right
        operations = 0  # Total operations to the right
        for i in range(n - 1, -1, -1):
            answer[i] += operations
            count += int(boxes[i])
            operations += count
        
        return answer
