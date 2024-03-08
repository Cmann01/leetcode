class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Sort the points based on x-coordinate
        points.sort(key=lambda x: x[0])
        
        max_width = 0
       
        for i in range(1, len(points)):
           
            width = points[i][0] - points[i-1][0]
            # Update max_width if the current width is greater
            max_width = max(max_width, width)
        
        return max_width


points1 = [[8,7],[9,9],[7,4],[9,7]]
points2 = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]

sol = Solution()
print(sol.maxWidthOfVerticalArea(points1)) # Output: 1
print(sol.maxWidthOfVerticalArea(points2)) # Output: 3
