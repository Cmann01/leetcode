class Solution:
    def recoverFromPreorder(self, traversal: str):
        self.i = 0  # Pointer to track position in traversal
        
        def dfs(depth: int):
            if self.i >= len(traversal):
                return None
            
            # Count dashes to determine depth level
            j = self.i
            while j < len(traversal) and traversal[j] == '-':
                j += 1
            dash_count = j - self.i  # Number of dashes
            
            # If dashes don't match expected depth, return
            if dash_count != depth:
                return None
            
            self.i += dash_count  # Move past dashes
            
            # Read node value
            value = 0
            while self.i < len(traversal) and traversal[self.i].isdigit():
                value = value * 10 + int(traversal[self.i])
                self.i += 1
            
            node = TreeNode(value)
            node.left = dfs(depth + 1)  # Process left child
            node.right = dfs(depth + 1)  # Process right child
            
            return node
        
        return dfs(0)  # Start recursion with depth 0
