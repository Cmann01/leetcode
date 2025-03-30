from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Step 1: Store the last occurrence index of each character
        last_index = {char: i for i, char in enumerate(s)}
        
        # Step 2: Initialize variables
        partitions = []
        start, end = 0, 0
        
        # Step 3: Iterate through the string to find partitions
        for i, char in enumerate(s):
            end = max(end, last_index[char])  # Extend the partition if needed
            if i == end:  # When we reach the end of a partition
                partitions.append(end - start + 1)
                start = i + 1  # Move the start to the next character
                
        return partitions