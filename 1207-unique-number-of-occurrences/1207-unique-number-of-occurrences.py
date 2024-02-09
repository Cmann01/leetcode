class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Count the occurrences of each number in the array
        count = {}
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Check if the number of occurrences is unique
        occurrences = set()
        for value in count.values():
            if value in occurrences:
                return False
            occurrences.add(value)
        
        return True

# Test cases
solution = Solution()
print(solution.uniqueOccurrences([1,2,2,1,1,3]))  # Output: True
print(solution.uniqueOccurrences([1,2]))          # Output: False
print(solution.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))  # Output: True
