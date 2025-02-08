import heapq

class NumberContainers:
    def __init__(self):
        self.index_to_number = {}  # Maps index -> number
        self.number_to_min_heap = {}  # Maps number -> min-heap of indices
        self.number_to_indices = {}  # Maps number -> set of indices

    def change(self, index: int, number: int) -> None:
        # If index already has a number, remove it from the old number's set
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            if old_number != number:
                self.number_to_indices[old_number].discard(index)
        
        # Assign the new number to the index
        self.index_to_number[index] = number
        
        # Maintain the heap for the new number
        if number not in self.number_to_min_heap:
            self.number_to_min_heap[number] = []
            self.number_to_indices[number] = set()
        
        heapq.heappush(self.number_to_min_heap[number], index)
        self.number_to_indices[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.number_to_min_heap or not self.number_to_indices[number]:
            return -1
        
        # Remove stale indices from the heap
        while self.number_to_min_heap[number] and self.number_to_min_heap[number][0] not in self.number_to_indices[number]:
            heapq.heappop(self.number_to_min_heap[number])

        return self.number_to_min_heap[number][0] if self.number_to_min_heap[number] else -1
