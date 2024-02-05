class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Check if the string is empty
        if not s:
            return 0
        
        # Function to check if a string is a palindrome
        def is_palindrome(string):
            return string == string[::-1]
        
        # If the string is already a palindrome, it can be removed in 1 step
        if is_palindrome(s):
            return 1
        else:
            # If it's not a palindrome, it means it contains both 'a' and 'b'
            # So, we can remove all 'a's and then all 'b's, which makes 2 steps
            return 2

# Test cases
solution = Solution()
print(solution.removePalindromeSub("ababa"))  # Output: 1
print(solution.removePalindromeSub("abb"))    # Output: 2
print(solution.removePalindromeSub("baabb"))  # Output: 2
