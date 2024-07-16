# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # Helper function to find the path from the root to a target node
        def findPath(root, target, path):
            if not root:
                return False
            if root.val == target:
                return True
            path.append('L')
            if findPath(root.left, target, path):
                return True
            path.pop()
            path.append('R')
            if findPath(root.right, target, path):
                return True
            path.pop()
            return False
        
        # Helper function to find the lowest common ancestor (LCA) of two nodes
        def findLCA(root, p, q):
            if not root or root.val == p or root.val == q:
                return root
            left = findLCA(root.left, p, q)
            right = findLCA(root.right, p, q)
            if left and right:
                return root
            return left if left else right

        # Find the LCA of startValue and destValue
        lca = findLCA(root, startValue, destValue)
        
        # Find the path from LCA to startValue
        path_to_start = []
        findPath(lca, startValue, path_to_start)
        
        # Find the path from LCA to destValue
        path_to_dest = []
        findPath(lca, destValue, path_to_dest)
        
        # The path to startValue needs to be reversed and turned into 'U'
        path_to_start = ['U'] * len(path_to_start)
        
        # Combine the paths
        return ''.join(path_to_start) + ''.join(path_to_dest)

# Example Usage:
# root = [5,1,2,3,null,6,4]
# startValue = 3
# destValue = 6
# sol = Solution()
# print(sol.getDirections(root, startValue, destValue))  # Output: "UURL"
