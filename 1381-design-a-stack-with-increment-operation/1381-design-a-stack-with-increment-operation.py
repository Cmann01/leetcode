class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        limit = min(k, len(self.stack))
        for i in range(limit):
            self.stack[i] += val


# Example Usage:
# Initialize the stack with a max size of 3
stk = CustomStack(3)

# Perform operations
stk.push(1)                          # stack becomes [1]
stk.push(2)                          # stack becomes [1, 2]
print(stk.pop())                     # returns 2, stack becomes [1]
stk.push(2)                          # stack becomes [1, 2]
stk.push(3)                          # stack becomes [1, 2, 3]
stk.push(4)                          # stack still [1, 2, 3], cannot add more
stk.increment(5, 100)                # stack becomes [101, 102, 103]
stk.increment(2, 100)                # stack becomes [201, 202, 103]
print(stk.pop())                     # returns 103, stack becomes [201, 202]
print(stk.pop())                     # returns 202, stack becomes [201]
print(stk.pop())                     # returns 201, stack becomes []
print(stk.pop())                     # returns -1, stack is empty
