# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        # Level-order traversal with a queue
        queue = [root]
        level = 0  # Root starts at level 0
        
        while queue:
            # Collect all nodes at the current level
            current_level_nodes = queue
            queue = []
            
            # Add children to the queue for the next level
            for node in current_level_nodes:
                if node.left and node.right:
                    queue.append(node.left)
                    queue.append(node.right)
            
            # Reverse values at odd levels
            if level % 2 == 1:
                # Reverse the node values at the current level
                values = [node.val for node in current_level_nodes]
                reversed_values = values[::-1]
                for node, val in zip(current_level_nodes, reversed_values):
                    node.val = val
            
            # Move to the next level
            level += 1
        
        return root
