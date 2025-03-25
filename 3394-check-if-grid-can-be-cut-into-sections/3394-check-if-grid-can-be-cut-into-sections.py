from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] < result[-1][1]:  # Overlapping
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
        
        return result

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        hor = []
        vert = []

        for x1, y1, x2, y2 in rectangles:
            hor.append([x1, x2])
            vert.append([y1, y2])
        
        if len(self.merge(hor)) >= 3:
            return True
        
        if len(self.merge(vert)) >= 3:
            return True
        
        return False
