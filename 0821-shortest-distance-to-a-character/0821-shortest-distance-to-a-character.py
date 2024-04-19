class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        n = len(s)
        ans = [float('inf')] * n
        prev = float('-inf')

        # Forward pass
        for i in range(n):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], i - prev)

        # Backward pass
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev - i)

        return ans
