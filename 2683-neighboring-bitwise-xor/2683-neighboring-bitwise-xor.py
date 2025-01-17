class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        n = len(derived)

        # Helper function to verify a given starting value
        def is_valid(start):
            original = [start]
            for i in range(n - 1):
                original.append(original[-1] ^ derived[i])
            # Check the circular condition
            return original[0] == (original[-1] ^ derived[-1])
        
        # Try both possible starting values for original[0]
        return is_valid(0) or is_valid(1)
