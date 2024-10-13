import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Create events: (time, type, friend_index)
        events = []
        for i, (arrive, leave) in enumerate(times):
            events.append((arrive, 'arrive', i))
            events.append((leave, 'leave', i))
        
        # Sort events by time; for same time, 'leave' should come before 'arrive'
        events.sort(key=lambda x: (x[0], x[1] == 'arrive'))
        
        # Min-heap to track available chairs
        available_chairs = []
        heapq.heapify(available_chairs)
        
        # Initially all chair indices are available, so we add chairs incrementally
        next_available_chair = 0
        
        # Dictionary to track which chair a friend is sitting on
        friend_to_chair = {}
        
        # Process events in sorted order
        for time, event_type, friend_index in events:
            if event_type == 'leave':
                # Free up the chair
                heapq.heappush(available_chairs, friend_to_chair[friend_index])
            else:  # event_type == 'arrive'
                # Assign the smallest available chair to this friend
                if available_chairs:
                    assigned_chair = heapq.heappop(available_chairs)
                else:
                    assigned_chair = next_available_chair
                    next_available_chair += 1
                
                friend_to_chair[friend_index] = assigned_chair
                
                # If this is the target friend, return the assigned chair
                if friend_index == targetFriend:
                    return assigned_chair
