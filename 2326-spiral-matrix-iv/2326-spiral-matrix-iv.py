class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode) -> List[List[int]]:
        # Initialize the matrix with -1
        matrix = [[-1] * n for _ in range(m)]
        
        # Define the boundaries
        top, bottom, left, right = 0, m - 1, 0, n - 1
        
        current_node = head
        
        while top <= bottom and left <= right and current_node:
            # Traverse from left to right along the top row
            for col in range(left, right + 1):
                if current_node:
                    matrix[top][col] = current_node.val
                    current_node = current_node.next
            top += 1
            
            # Traverse from top to bottom along the right column
            for row in range(top, bottom + 1):
                if current_node:
                    matrix[row][right] = current_node.val
                    current_node = current_node.next
            right -= 1
            
            # Traverse from right to left along the bottom row (if within bounds)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    if current_node:
                        matrix[bottom][col] = current_node.val
                        current_node = current_node.next
                bottom -= 1
            
            # Traverse from bottom to top along the left column (if within bounds)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    if current_node:
                        matrix[row][left] = current_node.val
                        current_node = current_node.next
                left += 1
        
        return matrix
