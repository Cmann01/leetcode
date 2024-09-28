class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [0] * k  # Initialize the deque with a fixed size of k
        self.front = 0  # Front pointer for the deque
        self.rear = 0   # Rear pointer for the deque
        self.capacity = k  # Capacity of the deque
        self.size = 0  # Current size of the deque

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        # Update front pointer in a circular manner
        self.front = (self.front - 1) % self.capacity
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque[self.rear] = value
        # Update rear pointer in a circular manner
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        # Move front pointer in a circular manner
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        # Move rear pointer in a circular manner
        self.rear = (self.rear - 1) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        # Rear points to the next empty slot, so the last element is at (rear - 1)
        return self.deque[(self.rear - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
