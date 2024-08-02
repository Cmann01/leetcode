class Solution:
    def minSwaps(self, nums):
        n = len(nums)
        totalOnes = sum(nums)
        
        if totalOnes == 0 or totalOnes == 1:
            return 0
        
        # Create an extended version of the array to handle circular nature
        extendedNums = nums + nums
        
        # Initialize the sliding window
        currentOnes = sum(extendedNums[:totalOnes])
        maxOnesInWindow = currentOnes
        
        # Slide the window across the array
        for i in range(1, n):
            currentOnes += extendedNums[i + totalOnes - 1] - extendedNums[i - 1]
            maxOnesInWindow = max(maxOnesInWindow, currentOnes)
        
        # The minimum number of swaps is the number of zeros in the best window
        return totalOnes - maxOnesInWindow

# Example usage:
solution = Solution()
print(solution.minSwaps([0,1,0,1,1,0,0]))  # Output: 1
print(solution.minSwaps([0,1,1,1,0,0,1,1,0]))  # Output: 2
print(solution.minSwaps([1,1,0,0,1]))  # Output: 0
