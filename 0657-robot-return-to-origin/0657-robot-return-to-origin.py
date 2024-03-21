class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
       
        horizontal = 0
        vertical = 0
        
        
        for move in moves:
            if move == 'U':
                vertical += 1
            elif move == 'D':
                vertical -= 1
            elif move == 'L':
                horizontal -= 1
            elif move == 'R':
                horizontal += 1
        
       
        return horizontal == 0 and vertical == 0


solution = Solution()
print(solution.judgeCircle("UD"))  # Output: True
print(solution.judgeCircle("LL"))  # Output: False
