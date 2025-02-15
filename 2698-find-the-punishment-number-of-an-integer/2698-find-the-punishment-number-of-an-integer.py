class Solution:
    def canPartition(self, s: str, target: int) -> bool:
        def dfs(index: int, current_sum: int) -> bool:
            if index == len(s):
                return current_sum == target
            for end in range(index + 1, len(s) + 1):
                num = int(s[index:end])
                if dfs(end, current_sum + num):
                    return True
            return False

        return dfs(0, 0)

    def punishmentNumber(self, n: int) -> int:
        total_sum = 0
        for i in range(1, n + 1):
            square_str = str(i * i)
            if self.canPartition(square_str, i):
                total_sum += i * i
        return total_sum

# Example usage
solution = Solution()
print(solution.punishmentNumber(10))  # Output: 182
print(solution.punishmentNumber(37))  # Output: 1478
