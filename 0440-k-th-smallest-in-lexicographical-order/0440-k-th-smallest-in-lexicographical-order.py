class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(curr, n):
            steps = 0
            first = curr
            last = curr
            while first <= n:
                steps += min(n + 1, last + 1) - first
                first *= 10
                last = last * 10 + 9
            return steps
        
        curr = 1
        k -= 1  # We start with the first number already taken
        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                # Skip this whole subtree
                curr += 1
                k -= steps
            else:
                # Go to the next level (deeper in the tree)
                curr *= 10
                k -= 1
        
        return curr