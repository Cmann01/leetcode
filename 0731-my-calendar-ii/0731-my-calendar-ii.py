class MyCalendarTwo:

    def __init__(self):
        self.events = []  # Store all successful events
        self.overlaps = []  # Store all double bookings (to prevent triple booking)

    def book(self, start: int, end: int) -> bool:
        # First, check if this new event overlaps with any double-booked intervals
        for ostart, oend in self.overlaps:
            if start < oend and end > ostart:  # If there is an overlap with a double booking
                return False  # Triple booking would happen, so reject this booking
        
        # Check for overlap with existing events, and record any double booking
        for estart, eend in self.events:
            if start < eend and end > estart:  # If there is an overlap with an event
                # Record the overlap as a double booking
                self.overlaps.append((max(start, estart), min(end, eend)))
        
        # Add the current event to the list of all events
        self.events.append((start, end))
        return True
