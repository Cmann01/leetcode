from collections import defaultdict

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = defaultdict(int)

        # Count the occurrences of each remainder when dividing by k
        for num in arr:
            remainder = num % k
            # Handle negative remainders by converting them to positive
            remainder_count[remainder] += 1

        # Now, check if we can pair all elements
        for remainder in remainder_count:
            if remainder == 0:
                # The number of elements with remainder 0 must be even
                if remainder_count[remainder] % 2 != 0:
                    return False
            else:
                complement = k - remainder
                if remainder_count[remainder] != remainder_count[complement]:
                    return False

        return True
