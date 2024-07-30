class Solution:
    def minimumDeletions(self, s: str) -> int:
        # Initial count of 'a's and 'b's
        count_a = s.count('a')
        count_b = 0
        min_deletions = count_a  # All 'a's need to be deleted if we encounter no 'b's
        
        for char in s:
            if char == 'a':
                # One 'a' is in the correct position, so we don't need to delete it
                count_a -= 1
            else:
                # We might need to delete this 'b'
                count_b += 1
            
            # The number of deletions needed if we balance at this point
            min_deletions = min(min_deletions, count_a + count_b)
        
        return min_deletions

# Example usage:
solution = Solution()
print(solution.minimumDeletions("aababbab"))  # Output: 2
print(solution.minimumDeletions("bbaaaaabb"))  # Output: 2
print(solution.minimumDeletions("b"))          # Output: 0
print(solution.minimumDeletions("aaa"))        # Output: 0
print(solution.minimumDeletions("bbbbb"))      # Output: 0
