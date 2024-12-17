import heapq
from collections import Counter

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Step 1: Count the frequency of each character
        freq = Counter(s)
        
        # Step 2: Use a max heap (negative frequencies for max behavior)
        max_heap = []
        for char, count in freq.items():
            heapq.heappush(max_heap, (-ord(char), count))  # Use -ord(char) for descending order
        
        result = []  # Result string
        prev_char = None  # Track previous character
        prev_count = 0     # Count of consecutive appearances of the previous character
        
        while max_heap:
            # Extract the largest available character
            char_neg, count = heapq.heappop(max_heap)
            char = chr(-char_neg)  # Convert back to character
            
            # Check if the current character violates the repeatLimit
            if prev_char == char and prev_count == repeatLimit:
                if not max_heap:
                    break  # No more characters to break the limit
                
                # Take the next largest character to break the sequence
                next_char_neg, next_count = heapq.heappop(max_heap)
                next_char = chr(-next_char_neg)
                
                result.append(next_char)
                if next_count > 1:
                    heapq.heappush(max_heap, (-ord(next_char), next_count - 1))
                
                # Put the original character back in the heap
                heapq.heappush(max_heap, (-ord(char), count))
                prev_char, prev_count = next_char, 1
            else:
                # Append the current character
                append_count = min(repeatLimit, count) if prev_char == char else min(count, repeatLimit)
                result.extend([char] * append_count)
                
                # Update the remaining count
                if count > append_count:
                    heapq.heappush(max_heap, (-ord(char), count - append_count))
                
                prev_char, prev_count = char, append_count
        
        return ''.join(result)
