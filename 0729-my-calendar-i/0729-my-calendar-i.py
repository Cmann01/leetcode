class MyCalendar:

    def __init__(self):
        # Store events as a list of tuples (start, end)
        self.events = []
        

    def book(self, start: int, end: int) -> bool:
        # Check for overlap with existing events
        for s, e in self.events:
            # If the start of the new event is before the end of an existing event
            # and the end of the new event is after the start of an existing event, it's an overlap
            if start < e and end > s:
                return False
        
        # If no overlap, add the event and return True
        self.events.append((start, end))
        return True
