class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Remove all underscores to compare relative orders of 'L' and 'R'
        start_pieces = [char for char in start if char != '_']
        target_pieces = [char for char in target if char != '_']
        
        # If the order of 'L' and 'R' is not the same, return False
        if start_pieces != target_pieces:
            return False
        
        # Use two pointers to validate movement constraints
        start_idx = 0
        target_idx = 0
        n = len(start)
        
        while start_idx < n and target_idx < n:
            # Skip underscores in start and target
            while start_idx < n and start[start_idx] == '_':
                start_idx += 1
            while target_idx < n and target[target_idx] == '_':
                target_idx += 1
            
            # If one pointer reaches the end, both must reach simultaneously
            if start_idx == n or target_idx == n:
                return start_idx == target_idx
            
            # If the characters differ, it's invalid
            if start[start_idx] != target[target_idx]:
                return False
            
            # Check movement constraints for 'L' and 'R'
            if start[start_idx] == 'L' and target_idx > start_idx:
                return False  # 'L' cannot move to the right
            if start[start_idx] == 'R' and target_idx < start_idx:
                return False  # 'R' cannot move to the left
            
            # Move both pointers to the next character
            start_idx += 1
            target_idx += 1
        
        return True
