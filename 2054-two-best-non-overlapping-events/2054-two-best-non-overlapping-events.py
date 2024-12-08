from bisect import bisect_right

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort events by end time
        events.sort(key=lambda x: x[1])
        
        # Initialize variables
        max_value = 0
        max_sum = 0
        ends = []  # Store end times
        max_values = []  # Store max value up to each end time
        
        for start, end, value in events:
            # Binary search to find the latest non-overlapping event
            idx = bisect_right(ends, start - 1) - 1
            
            # Calculate the max value considering two non-overlapping events
            if idx >= 0:
                max_sum = max(max_sum, max_values[idx] + value)
            else:
                max_sum = max(max_sum, value)  # Single event case
            
            # Update the max value seen so far
            max_value = max(max_value, value)
            
            # Update tracking lists
            ends.append(end)
            max_values.append(max_value)
        
        return max_sum
