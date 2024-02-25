class Solution:
    def sumOfMultiples(self, n: int) -> int:
        total_sum = 0
        for num in range(1, n + 1):
            if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
                total_sum += num
        return total_sum

# Test cases
solution = Solution()
print(solution.sumOfMultiples(7))  # Output: 21
print(solution.sumOfMultiples(10))  # Output: 40
print(solution.sumOfMultiples(9))   # Output: 30
