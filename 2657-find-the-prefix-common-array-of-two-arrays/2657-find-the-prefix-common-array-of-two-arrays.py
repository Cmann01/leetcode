from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        C = [0] * n  # Initialize the result array
        seen = set()  # Set to track seen elements in A and B
        common_count = 0  # Counter for common elements

        for i in range(n):
            # Add current elements of A and B to the seen set
            if A[i] in seen:
                common_count += 1
            else:
                seen.add(A[i])

            if B[i] in seen:
                common_count += 1
            else:
                seen.add(B[i])

            # Update the prefix common count
            C[i] = common_count

        return C
