class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Initialize an array to store cumulative shift values
        n = len(s)
        shift_array = [0] * (n + 1)
        
        # Process the shifts and update the shift_array
        for start, end, direction in shifts:
            if direction == 1:
                shift_array[start] += 1
                shift_array[end + 1] -= 1
            else:
                shift_array[start] -= 1
                shift_array[end + 1] += 1
        
        # Apply prefix sum to calculate the net shift for each character
        for i in range(1, n):
            shift_array[i] += shift_array[i - 1]
        
        # Build the resulting string after applying the shifts
        result = []
        for i in range(n):
            # Calculate the new character after shifting
            shift = shift_array[i] % 26
            new_char = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
        
        return ''.join(result)
