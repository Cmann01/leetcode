class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        xor1, xor2 = 0, 0
        
        # XOR of all elements in nums1
        for num in nums1:
            xor1 ^= num
        
        # XOR of all elements in nums2
        for num in nums2:
            xor2 ^= num
        
        # Final XOR result
        result = 0
        if len(nums2) % 2 == 1:  # If nums2 length is odd
            result ^= xor1
        if len(nums1) % 2 == 1:  # If nums1 length is odd
            result ^= xor2
        
        return result
