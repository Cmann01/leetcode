class Solution:
    def minSwaps(self, s: str) -> int:
        # `balance` keeps track of imbalance of brackets
        balance = 0
        swaps_needed = 0
        
        for bracket in s:
            if bracket == '[':
                balance += 1
            else:
                balance -= 1
            
            # If balance goes negative, we need a swap
            if balance < 0:
                swaps_needed += 1
                # Reset the balance by swapping an opening bracket
                balance = 1  # As after the swap, we will have one more opening bracket
        
        return swaps_needed
