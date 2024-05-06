# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        
        # Reverse the linked list
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Now traverse the reversed list to remove nodes with smaller values
        max_value = float('-inf')
        dummy = ListNode(0)
        dummy.next = prev
        current = dummy
        
        while current and current.next:
            if current.next.val < max_value:
                current.next = current.next.next
            else:
                max_value = current.next.val
                current = current.next
        
        # Reverse the list again to get the original order
        prev = None
        current = dummy.next
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev
