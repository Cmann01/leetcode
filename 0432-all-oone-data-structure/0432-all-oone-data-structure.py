class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()  # Use a set to store keys with this count
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        # Initialize the key -> node mapping
        self.key_count_map = {}
        # Initialize the doubly linked list with dummy head and tail
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # Add a new node with a given count after the specified node
    def _add_node_after(self, prev_node, count):
        new_node = Node(count)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next.prev = new_node
        prev_node.next = new_node
        return new_node

    # Remove a node from the doubly linked list
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # Increment the count of the key by 1
    def inc(self, key: str) -> None:
        if key not in self.key_count_map:
            # Key does not exist, add it with count 1
            if self.head.next == self.tail or self.head.next.count != 1:
                new_node = self._add_node_after(self.head, 1)
            self.head.next.keys.add(key)
            self.key_count_map[key] = self.head.next
        else:
            # Key exists, increment its count
            cur_node = self.key_count_map[key]
            new_count = cur_node.count + 1
            if cur_node.next == self.tail or cur_node.next.count != new_count:
                new_node = self._add_node_after(cur_node, new_count)
            else:
                new_node = cur_node.next
            new_node.keys.add(key)
            self.key_count_map[key] = new_node
            # Remove the key from the current node
            cur_node.keys.remove(key)
            if not cur_node.keys:
                self._remove_node(cur_node)

    # Decrement the count of the key by 1
    def dec(self, key: str) -> None:
        if key not in self.key_count_map:
            return
        cur_node = self.key_count_map[key]
        if cur_node.count == 1:
            # If the count becomes zero, remove the key completely
            del self.key_count_map[key]
        else:
            new_count = cur_node.count - 1
            if cur_node.prev == self.head or cur_node.prev.count != new_count:
                new_node = self._add_node_after(cur_node.prev, new_count)
            else:
                new_node = cur_node.prev
            new_node.keys.add(key)
            self.key_count_map[key] = new_node
        # Remove the key from the current node
        cur_node.keys.remove(key)
        if not cur_node.keys:
            self._remove_node(cur_node)

    # Get the key with the maximum count
    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    # Get the key with the minimum count
    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))

# Example Usage:
# obj = AllOne()
# obj.inc("hello")
# obj.inc("hello")
# print(obj.getMaxKey())  # Expected: "hello"
# print(obj.getMinKey())  # Expected: "hello"
# obj.inc("leet")
# print(obj.getMaxKey())  # Expected: "hello"
# print(obj.getMinKey())  # Expected: "leet"
