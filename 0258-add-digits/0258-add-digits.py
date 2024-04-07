class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        else:
            return 1 + ((num - 1) % 9)


solution = Solution()
print(solution.addDigits(38))  # Output: 2
print(solution.addDigits(0))   # Output: 0
