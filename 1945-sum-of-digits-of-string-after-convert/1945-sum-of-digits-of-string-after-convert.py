class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Step 1: Convert the string to a number by replacing letters with their positions in the alphabet
        num_str = ''.join(str(ord(char) - ord('a') + 1) for char in s)
        
        # Step 2: Perform the sum of digits transformation k times
        for _ in range(k):
            num_str = str(sum(int(digit) for digit in num_str))
        
        # The final number after k transformations
        return int(num_str)
