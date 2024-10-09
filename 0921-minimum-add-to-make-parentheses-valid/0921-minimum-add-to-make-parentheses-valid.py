class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Counters for unmatched parentheses
        open_count = 0  # Unmatched '('
        close_count = 0  # Unmatched ')'
        
        for char in s:
            if char == '(':
                open_count += 1  # We have an unmatched '('
            elif char == ')':
                if open_count > 0:  # There is an unmatched '(' to balance with ')'
                    open_count -= 1  # Match it, so reduce the count of '('
                else:
                    close_count += 1  # No unmatched '(', so we need to add '('
        
        # The result is the sum of unmatched '(' and unmatched ')'
        return open_count + close_count
