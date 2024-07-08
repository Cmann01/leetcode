class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0  # J(1, k) = 0
        for i in range(2, n+1):
            winner = (winner + k) % i
        return winner + 1  # convert zero-based index to one-based

# Example usage
solution = Solution()
print(solution.findTheWinner(5, 2))  # Output: 3
print(solution.findTheWinner(6, 5))  # Output: 1
