class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        
        # Convert each interval into two events
        for left, right in intervals:
            events.append((left, 1))   # 1 means an interval starts
            events.append((right + 1, -1))  # -1 means an interval ends (after 'right')
        
        # Sort events; if two events have the same position, process the end event first
        events.sort()
        
        max_groups = 0
        current_groups = 0
        
        # Process events
        for event in events:
            current_groups += event[1]  # Update active intervals count
            max_groups = max(max_groups, current_groups)
        
        return max_groups
