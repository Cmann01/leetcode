class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert time to minutes
        def convertToMinutes(time: str) -> int:
            h, m = map(int, time.split(":"))
            return h * 60 + m
        
        # Convert all time points to minutes
        minutes = [convertToMinutes(tp) for tp in timePoints]
        
        # Sort the list of minutes
        minutes.sort()
        
        # Initialize minimum difference to a large number
        min_diff = float('inf')
        
        # Calculate the difference between consecutive time points
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        
        # Also check the difference between the first and last time points across midnight
        min_diff = min(min_diff, (1440 - minutes[-1] + minutes[0]))
        
        return min_diff
