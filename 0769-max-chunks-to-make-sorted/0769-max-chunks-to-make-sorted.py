class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        max_so_far = 0  # Keeps track of the maximum value encountered so far
        chunks = 0  # Counts the number of chunks
        
        for i in range(len(arr)):
            max_so_far = max(max_so_far, arr[i])  # Update the maximum value
            if max_so_far == i:  # If max_so_far equals the current index
                chunks += 1  # We can form a chunk
        
        return chunks
