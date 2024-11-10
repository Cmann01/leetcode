from typing import List

class Solution:
    def update(self, number: int, vec: List[int], val: int):
        # Update the count of set bits in each position
        for i in range(32):  # 32 bits for handling integers up to 2^31 - 1
            if (number >> i) & 1:
                vec[i] += val

    def getDecimalFromBinary(self, vec: List[int]) -> int:
        # Convert the bit vector back to a decimal integer
        num = 0
        for i in range(32):
            if vec[i] > 0:  # If there are set bits in this position
                num |= (1 << i)
        return num

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = float('inf')
        i = 0
        j = 0
        vec = [0] * 32  # List to store count of set bits for each position

        while j < n:
            # Expand the window by including nums[j]
            self.update(nums[j], vec, 1)

            # Shrink the window from the left while the condition is met
            while i <= j and self.getDecimalFromBinary(vec) >= k:
                result = min(result, j - i + 1)
                self.update(nums[i], vec, -1)
                i += 1

            j += 1

        return result if result != float('inf') else -1
