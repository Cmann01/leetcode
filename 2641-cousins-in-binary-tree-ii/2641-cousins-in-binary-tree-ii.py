from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        # First pass: Compute the sum of each level
        queue = deque([root])
        levelSum = []
        
        # Step 1: Find the sum of each level and store in levelSum
        while queue:
            currLevelSum = 0
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                currLevelSum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            levelSum.append(currLevelSum)
        
        # Second pass: Replace each node's value with the sum of cousins
        queue = deque([root])
        root.val = 0  # Root has no cousins
        level = 1  # Start from level 1 (root is at level 0)
        
        # Step 2: Update node values with cousin sum
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                
                # Calculate the sum of the node's siblings
                siblingSum = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
                
                # Update the values of the left and right children
                if node.left:
                    node.left.val = levelSum[level] - siblingSum
                    queue.append(node.left)
                if node.right:
                    node.right.val = levelSum[level] - siblingSum
                    queue.append(node.right)
            
            level += 1
        
        return root
