# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # Base cases: If both nodes are None, they are equal.
        if not p and not q:
            return True
        # If one of the nodes is None and the other is not, they are not equal.
        if not p or not q:
            return False
        # If the values are not equal, they are not equal trees.
        if p.val != q.val:
            return False
        
        # Recursively check the left and right subtrees.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Example usage:
# Create tree nodes based on the given input examples.
p1 = TreeNode(1, TreeNode(2), TreeNode(3))
q1 = TreeNode(1, TreeNode(2), TreeNode(3))

p2 = TreeNode(1, TreeNode(2), None)
q2 = TreeNode(1, None, TreeNode(2))

p3 = TreeNode(1, TreeNode(2), TreeNode(1))
q3 = TreeNode(1, TreeNode(1), TreeNode(2))

# Create a Solution object and test the isSameTree function.
sol = Solution()
print(sol.isSameTree(p1, q1))  # Output: True
print(sol.isSameTree(p2, q2))  # Output: False
print(sol.isSameTree(p3, q3))  # Output: False
