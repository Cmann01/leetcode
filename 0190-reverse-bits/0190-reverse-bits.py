class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # Convert the input integer to a binary string and remove the '0b' prefix
        binary_str = bin(n)[2:]

        # Ensure the binary string has a length of 32 by padding with zeros if needed
        binary_str = binary_str.zfill(32)

        # Reverse the binary string
        reversed_str = binary_str[::-1]

        # Convert the reversed binary string back to an integer
        reversed_int = int(reversed_str, 2)

        return reversed_int

# Example usage:
solution = Solution()
result = solution.reverseBits(0b00000010100101000001111010011100)
print(result)  # Output: 964176192
