class Solution:
    def minEnd(self, n: int, x: int) -> int:
        incr = n - 1
        ans = 0

        # Iterate through each bit position (64 bits is enough for int in Python)
        for i in range(64):
            if (x & (1 << i)) > 0:
                # If the i-th bit of x is set, set the i-th bit of the answer
                ans |= (1 << i)
            else:
                # If the i-th bit of x is not set, adjust according to incr
                if incr & 1:
                    ans |= (1 << i)
                incr >>= 1  # Right shift incr to process the next bit

        return ans
