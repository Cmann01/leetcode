from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        # Initialize arrays for level, height, max and second max heights at each level
        self.level = [0] * 1000001  # Level of each node
        self.height = [0] * 100001  # Height of each node
        self.levelMaxHt = [0] * 100001  # Max height at each level
        self.levelSecondMaxHt = [0] * 100001  # Second max height at each level

    # Helper function to calculate the height of each node and store level info
    def findHeight(self, root: Optional[TreeNode], l: int) -> int:
        if not root:
            return 0

        # Set the level of the current node
        self.level[root.val] = l
        # Calculate height of current node's subtree
        self.height[root.val] = max(self.findHeight(root.left, l + 1), self.findHeight(root.right, l + 1)) + 1

        # Update levelMaxHt and levelSecondMaxHt arrays
        if self.levelMaxHt[l] < self.height[root.val]:
            self.levelSecondMaxHt[l] = self.levelMaxHt[l]
            self.levelMaxHt[l] = self.height[root.val]
        elif self.levelSecondMaxHt[l] < self.height[root.val]:
            self.levelSecondMaxHt[l] = self.height[root.val]

        return self.height[root.val]

    # Main function to answer queries
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # Populate level and height information
        self.findHeight(root, 0)

        result = []
        for node in queries:
            # Get the level of the queried node
            L = self.level[node]

            # Calculate the height of the tree if the subtree rooted at `node` is removed
            tempResult = L + (self.levelSecondMaxHt[L] if self.levelMaxHt[L] == self.height[node] else self.levelMaxHt[L]) - 1

            result.append(tempResult)

        return result
