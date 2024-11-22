from collections import defaultdict

class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # To store frequency of row patterns
        pattern_count = defaultdict(int)
        
        # Iterate through each row in the matrix
        for row in matrix:
            # Create a tuple of differences relative to the first column
            # and normalize it so that we compare rows that can become identical after flips
            flipped_pattern = tuple(1 - x for x in row)
            pattern_count[tuple(row)] += 1
            pattern_count[flipped_pattern] += 1
            
        # The result is the maximum count of any pattern
        return max(pattern_count.values())

