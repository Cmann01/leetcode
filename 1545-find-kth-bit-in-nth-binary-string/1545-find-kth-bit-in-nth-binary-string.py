class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Helper function to recursively find the kth bit
        def find_kth_bit(n, k):
            # Base case: If n == 1, return the only bit in S1, which is '0'
            if n == 1:
                return '0'
            
            length = (1 << n) - 1  # Length of Sn, which is 2^n - 1
            mid = length // 2 + 1  # The middle position
            
            if k == mid:
                return '1'
            elif k < mid:
                return find_kth_bit(n - 1, k)
            else:
                # Find the mirrored and inverted bit
                mirror_pos = length - k + 1
                mirrored_bit = find_kth_bit(n - 1, mirror_pos)
                return '0' if mirrored_bit == '1' else '1'
        
        return find_kth_bit(n, k)
