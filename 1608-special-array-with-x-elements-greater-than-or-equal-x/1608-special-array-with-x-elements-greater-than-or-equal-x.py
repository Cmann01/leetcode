class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()  
        n = len(nums)
        
        for x in range(n+1):
            count = 0
            for num in nums:
                if num >= x:
                    count += 1
            if count == x:
                return x
        return -1


solution = Solution()
print(solution.specialArray([3,5]))  # Output: 2
print(solution.specialArray([0,0]))  # Output: -1
print(solution.specialArray([0,4,3,0,4]))  # Output: 3
