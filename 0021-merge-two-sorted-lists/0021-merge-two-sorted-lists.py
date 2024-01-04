# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to serve as the head of the merged list
        dummy = ListNode()
        # Pointer to the current node in the merged list
        current = dummy

        # Iterate through both lists until one of them is empty
        while list1 is not None and list2 is not None:
            # Compare values of the current nodes in both lists
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            # Move the current pointer to the newly added node
            current = current.next

        # If one of the lists is not empty, append the remaining nodes
        if list1 is not None:
            current.next = list1
        elif list2 is not None:
            current.next = list2

        # The merged list starts from the next of the dummy node
        return dummy.next
