class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # Handling edge case where head is None
        while head and head.val == val:
            head = head.next
        
        # If head is None or there's only one node
        if not head:
            return None

        current = head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head

# Example usage:
# Construct the linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

# Create an instance of the Solution class
sol = Solution()

# Call the removeElements method
new_head = sol.removeElements(head, 6)

# Print the result
while new_head:
    print new_head.val,
    new_head = new_head.next
