class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]  # Adding 1 to convert from 0-indexed to 1-indexed
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        # If no solution is found
        return []
