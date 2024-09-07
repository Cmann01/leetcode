# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        
        # Helper function to check if linked list matches starting from the given tree node
        def checkPath(head, node):
            if not head:  # If we've reached the end of the linked list, return True
                return True
            if not node:  # If we've reached a null node in the tree but the list isn't finished, return False
                return False
            if head.val != node.val:  # If values don't match, return False
                return False
            
            # Continue checking the linked list in the left or right subtree
            return checkPath(head.next, node.left) or checkPath(head.next, node.right)
        
        if not root:
            return False
        
        # Check for matching path from the current node or start from left/right subtree
        return checkPath(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

