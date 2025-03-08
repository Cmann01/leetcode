class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_operations = float('inf')
        white_count = 0
        
        # Count white blocks in the first window of size k
        for i in range(k):
            if blocks[i] == 'W':
                white_count += 1
        
        min_operations = white_count
        
        # Slide the window across the string
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':  # Remove the leftmost element of the previous window
                white_count -= 1
            if blocks[i] == 'W':  # Add the new rightmost element of the current window
                white_count += 1
            
            min_operations = min(min_operations, white_count)
        
        return min_operations