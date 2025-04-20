from typing import List
from collections import Counter
import math

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        total = 0
        for k, count in counter.items():
            group_size = k + 1
            groups = math.ceil(count / group_size)
            total += groups * group_size
        return total
