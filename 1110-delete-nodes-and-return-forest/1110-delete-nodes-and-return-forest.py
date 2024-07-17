from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        result = []

        def dfs(node: Optional[TreeNode], is_root: bool) -> Optional[TreeNode]:
            if not node:
                return None
            
            # Check if this node needs to be a new root
            root_deleted = node.val in to_delete_set
            if is_root and not root_deleted:
                result.append(node)
            
            # Recur for left and right children
            node.left = dfs(node.left, root_deleted)
            node.right = dfs(node.right, root_deleted)
            
            return None if root_deleted else node
        
        dfs(root, True)
        return result
