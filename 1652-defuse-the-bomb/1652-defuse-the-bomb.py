from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        
        result = [0] * n
        for i in range(n):
            if k > 0:
                # Sum of the next k numbers
                result[i] = sum(code[(i + j) % n] for j in range(1, k + 1))
            elif k < 0:
                # Sum of the previous k numbers
                result[i] = sum(code[(i + j) % n] for j in range(k, 0))
        return result
