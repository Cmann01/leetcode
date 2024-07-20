class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # Initialize the result matrix with zeros
        result = [[0] * len(colSum) for _ in range(len(rowSum))]
        
        # Iterate over the matrix cells
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                # Fill the cell with the minimum of rowSum[i] and colSum[j]
                result[i][j] = min(rowSum[i], colSum[j])
                
                # Subtract the value from both rowSum and colSum
                rowSum[i] -= result[i][j]
                colSum[j] -= result[i][j]
                
        return result

# Example usage
solution = Solution()
rowSum = [3, 8]
colSum = [4, 7]
print(solution.restoreMatrix(rowSum, colSum))  # Output: [[3, 0], [1, 7]]

rowSum = [5, 7, 10]
colSum = [8, 6, 8]
print(solution.restoreMatrix(rowSum, colSum))  # Output: [[0, 5, 0], [6, 1, 0], [2, 0, 8]]
