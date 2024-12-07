class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def canDivide(maxPenalty):
            operations = 0
            for balls in nums:
                # Calculate the number of splits needed for this bag
                operations += (balls - 1) // maxPenalty
                if operations > maxOperations:
                    return False
            return True
        
        left, right = 1, max(nums)  # Search range for the penalty
        result = right
        
        while left <= right:
            mid = (left + right) // 2
            if canDivide(mid):
                result = mid  # Update the result if feasible
                right = mid - 1  # Try smaller penalties
            else:
                left = mid + 1  # Try larger penalties
        
        return result
