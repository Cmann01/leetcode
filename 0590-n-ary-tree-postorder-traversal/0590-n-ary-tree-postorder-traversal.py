"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # If root is None, return an empty list
        if not root:
            return []
        
        result = []
        
        # Helper function to perform postorder traversal recursively
        def traverse(node):
            # Traverse all the children first
            for child in node.children:
                traverse(child)
            # After traversing the children, add the node's value
            result.append(node.val)
        
        # Start the traversal from the root
        traverse(root)
        
        return result
