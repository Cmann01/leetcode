class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Start from the rightmost digit
        for i in range(len(digits) - 1, -1, -1):
            # Increment the current digit
            digits[i] += 1
            
            # Check if there's a carry
            if digits[i] == 10:
                digits[i] = 0  # Set current digit to 0
            else:
                # No carry, we can stop here
                return digits
        
        # If we're here, it means there was a carry from the leftmost digit
        # Add a new digit 1 at the beginning
        digits.insert(0, 1)
        
        return digits
