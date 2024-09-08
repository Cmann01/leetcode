# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: ListNode, k: int):
        # Step 1: Calculate the length of the list
        current = head
        n = 0
        while current:
            n += 1
            current = current.next
            
        # Step 2: Determine the size of each part
        part_size = n // k  # Minimum size of each part
        remainder = n % k    # Extra nodes to distribute

        # Step 3: Split the linked list
        parts = []
        current = head
        for i in range(k):
            part_head = current  # Start of the current part
            # Determine the size of the current part
            current_part_size = part_size + (1 if remainder > 0 else 0)
            remainder -= 1
            
            # Move `current` to the end of the current part
            for j in range(current_part_size - 1):
                if current:
                    current = current.next
            
            # Break the link to the next part
            if current:
                next_part = current.next
                current.next = None
                current = next_part
            
            # Add the head of the current part to the result
            parts.append(part_head)
        
        # Step 4: Add empty parts if there are less than `k` parts
        while len(parts) < k:
            parts.append(None)
        
        return parts
