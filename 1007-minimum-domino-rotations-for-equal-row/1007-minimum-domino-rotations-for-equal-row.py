from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            rotations_top = rotations_bottom = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return -1  # Neither side has x, so it's impossible
                elif tops[i] != x:
                    rotations_top += 1
                elif bottoms[i] != x:
                    rotations_bottom += 1
            return min(rotations_top, rotations_bottom)

        result = check(tops[0])
        if result != -1:
            return result
        # Only check bottoms[0] if it's different from tops[0]
        return check(bottoms[0]) if tops[0] != bottoms[0] else -1
