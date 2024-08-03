from collections import Counter
from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # Check if both arrays have the same elements with the same frequencies
        return Counter(target) == Counter(arr)
