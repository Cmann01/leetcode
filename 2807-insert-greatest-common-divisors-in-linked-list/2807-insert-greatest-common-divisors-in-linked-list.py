from math import gcd
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list has only one node or is empty, return the list as is
        if not head or not head.next:
            return head
        
        current = head
        
        # Traverse the list until the second last node
        while current and current.next:
            # Calculate the GCD of current node value and next node value
            gcd_value = gcd(current.val, current.next.val)
            
            # Create a new node with the gcd_value
            new_node = ListNode(val=gcd_value)
            
            # Insert the new node between current and next
            new_node.next = current.next
            current.next = new_node
            
            # Move to the next pair of nodes (skip the newly inserted node)
            current = new_node.next
        
        return head
