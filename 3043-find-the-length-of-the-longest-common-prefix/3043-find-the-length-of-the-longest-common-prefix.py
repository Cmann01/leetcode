class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # Helper function to calculate the common prefix length of two numbers
        def common_prefix_length(a: int, b: int) -> int:
            # Convert both numbers to strings to compare prefixes
            str_a = str(a)
            str_b = str(b)
            i = 0
            # Compare digit by digit
            while i < len(str_a) and i < len(str_b) and str_a[i] == str_b[i]:
                i += 1
            return i
        
        # Sort both arrays by the string representation of the numbers
        arr1 = sorted(arr1, key=str)
        arr2 = sorted(arr2, key=str)
        
        # Initialize pointers and max length
        i, j = 0, 0
        max_common_prefix_length = 0
        
        # Two-pointer approach to compare only relevant pairs
        while i < len(arr1) and j < len(arr2):
            # Compare arr1[i] and arr2[j]
            max_common_prefix_length = max(max_common_prefix_length, common_prefix_length(arr1[i], arr2[j]))
            
            # Move the pointer with the smaller value to keep exploring
            if str(arr1[i]) < str(arr2[j]):
                i += 1
            else:
                j += 1
        
        return max_common_prefix_length
