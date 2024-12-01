from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # Create a set to store visited numbers
        seen = set()
        
        for num in arr:
            # Check if the double of the current number or half of it (if even) exists in the set
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            # Add the current number to the set
            seen.add(num)
        
        # If no such pair is found, return False
        return False
