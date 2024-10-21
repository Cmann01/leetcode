class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # Helper function for backtracking
        def backtrack(start: int, seen: set) -> int:
            if start == len(s):
                return 0  # If we have reached the end, no more splits to make
            
            max_splits = 0
            for end in range(start + 1, len(s) + 1):
                # Get the current substring
                substring = s[start:end]
                if substring not in seen:
                    # Add the substring to the set and explore further
                    seen.add(substring)
                    # Recursively backtrack to explore further splits
                    max_splits = max(max_splits, 1 + backtrack(end, seen))
                    # Backtrack: remove the substring to try other possibilities
                    seen.remove(substring)
            return max_splits
        
        # Start backtracking from index 0 with an empty set of seen substrings
        return backtrack(0, set())
