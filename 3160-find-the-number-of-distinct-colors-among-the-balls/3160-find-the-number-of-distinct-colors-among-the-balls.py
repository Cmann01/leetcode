from typing import List
from collections import defaultdict

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colors = {}  # Maps each ball to its current color
        color_count = defaultdict(int)  # Counts occurrences of each color
        distinct_colors = 0  # Tracks the number of distinct colors
        results = []
        
        for ball, color in queries:
            if ball in ball_colors:
                prev_color = ball_colors[ball]
                if prev_color == color:
                    # If the color is unchanged, just append the current count
                    results.append(distinct_colors)
                    continue
                
                # Decrease count of previous color
                color_count[prev_color] -= 1
                if color_count[prev_color] == 0:
                    distinct_colors -= 1  # Remove from distinct count

            # Assign new color
            ball_colors[ball] = color
            
            # Increase count of new color
            if color_count[color] == 0:
                distinct_colors += 1  # New distinct color
            color_count[color] += 1
            
            results.append(distinct_colors)
        
        return results

# Example usage:
solution = Solution()
limit = 1
queries = [[0,1],[0,4],[0,4],[0,1],[1,2]]
print(solution.queryResults(limit, queries))  # Output: [1, 1, 1, 1, 2]

