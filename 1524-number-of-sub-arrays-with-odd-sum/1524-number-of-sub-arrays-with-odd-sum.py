from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1  # Empty prefix sum is considered even
        prefix_sum = 0
        result = 0

        for num in arr:
            prefix_sum += num  # Update running sum

            if prefix_sum % 2 == 0:
                result += odd_count  # Odd subarrays end at this point
                even_count += 1
            else:
                result += even_count  # Even subarrays form odd subarrays
                odd_count += 1

            result %= MOD  # Keep result within mod constraint

        return result
