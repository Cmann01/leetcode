class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # List of valid characters
        chars = ['a', 'b', 'c']
        result = []

        # Helper function for backtracking
        def backtrack(current_string):
            # If the current string has length n, add it to the result
            if len(current_string) == n:
                result.append(current_string)
                return

            # Try adding each character and ensure no consecutive duplicates
            for char in chars:
                if not current_string or current_string[-1] != char:
                    backtrack(current_string + char)

        # Start backtracking with an empty string
        backtrack("")

        # Check if k is within the bounds of the result list
        if k > len(result):
            return ""
        return result[k - 1]

# Example usage
sol = Solution()
print(sol.getHappyString(1, 3))  # Output: "c"
print(sol.getHappyString(1, 4))  # Output: ""
print(sol.getHappyString(3, 9))  # Output: "cab"
