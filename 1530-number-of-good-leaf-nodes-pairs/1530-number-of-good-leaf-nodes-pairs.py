# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0
        
        def dfs(node):
            if not node:
                return []
            
            if not node.left and not node.right:  # If it's a leaf node
                return [1]
            
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            # Check all pairs of distances from left and right subtrees
            for l in left_distances:
                for r in right_distances:
                    if l + r <= distance:
                        self.result += 1
            
            # Return all distances incremented by 1
            return [n + 1 for n in left_distances + right_distances if n + 1 <= distance]
        
        dfs(root)
        return self.result

# Example usage
# root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
# distance = 3
# solution = Solution()
# print(solution.countPairs(root, distance))  # Output: 1
