# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize an empty list to store the result
        result = []
        
        # Helper function to perform the recursive traversal
        def traverse(node):
            if node:
                # Recursively traverse the left subtree
                traverse(node.left)
                # Recursively traverse the right subtree
                traverse(node.right)
                # Add the root node's value to the result
                result.append(node.val)
        
        # Start the traversal from the root
        traverse(root)
        
        return result
