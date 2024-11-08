from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # Step 1: Calculate the XOR of the entire array
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
            
        # Step 2: Determine the maximum value for maximumBit bits
        max_val = (1 << maximumBit) - 1  # This is 2^maximumBit - 1
        
        # Step 3: Initialize the answer array
        answer = []
        
        # Step 4: Process each element in reverse
        for i in range(len(nums)):
            # Find k to maximize the XOR with xor_sum
            k = max_val ^ xor_sum
            answer.append(k)
            
            # Update xor_sum by removing the last element in the remaining array
            xor_sum ^= nums[-1]
            nums.pop()  # Remove the last element as per the problem statement
            
        return answer
