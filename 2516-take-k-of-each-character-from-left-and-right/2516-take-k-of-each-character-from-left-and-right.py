class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        from collections import Counter
        
        # Count total occurrences of each character
        total_count = Counter(s)
        if total_count['a'] < k or total_count['b'] < k or total_count['c'] < k:
            return -1
        
        # Target counts after taking k of each character
        target = {
            'a': total_count['a'] - k,
            'b': total_count['b'] - k,
            'c': total_count['c'] - k
        }
        
        # Sliding window to find the longest substring satisfying the target
        n = len(s)
        left = 0
        current_count = {'a': 0, 'b': 0, 'c': 0}
        max_window_length = 0
        
        for right in range(n):
            current_count[s[right]] += 1
            
            # Shrink the window if any character count exceeds the target
            while current_count['a'] > target['a'] or current_count['b'] > target['b'] or current_count['c'] > target['c']:
                current_count[s[left]] -= 1
                left += 1
            
            # Update the maximum window length
            max_window_length = max(max_window_length, right - left + 1)
        
        # Minimum time = Total length - Max window length
        return n - max_window_length
