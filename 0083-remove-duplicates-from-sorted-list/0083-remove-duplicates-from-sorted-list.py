# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Check if the linked list is empty or has only one node
        if not head or not head.next:
            return head

        current = head

        # Traverse the linked list
        while current.next:
            # If the current node's value is equal to the next node's value, skip the next node
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next

        return head