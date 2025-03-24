from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days
        
        # Step 1: Sort the meetings by start time
        meetings.sort()
        
        # Step 2: Merge intervals and count occupied days
        occupied_days = 0
        prev_start, prev_end = meetings[0]
        
        for start, end in meetings[1:]:
            if start <= prev_end:  # Overlapping interval
                prev_end = max(prev_end, end)
            else:  # Non-overlapping interval
                occupied_days += (prev_end - prev_start + 1)
                prev_start, prev_end = start, end
        
        # Step 3: Add the last merged interval
        occupied_days += (prev_end - prev_start + 1)
        
        # Step 4: Compute available days
        return days - occupied_days
