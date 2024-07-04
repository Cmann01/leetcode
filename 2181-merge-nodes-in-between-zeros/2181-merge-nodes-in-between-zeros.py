# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        # Skip the initial 0 node
        current = head.next
        
        # Initialize the list to store the sums
        sums = []
        
        # Variable to keep track of the current sum between two 0s
        current_sum = 0
        
        while current:
            if current.val == 0:
                if current_sum != 0:
                    sums.append(current_sum)
                    current_sum = 0
            else:
                current_sum += current.val
            current = current.next
        
        # Create the new linked list with the sums
        dummy = ListNode(0)
        tail = dummy
        for s in sums:
            tail.next = ListNode(s)
            tail = tail.next
        
        return dummy.next
