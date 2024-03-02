class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        frequency = {}
        
       
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
       
        unique_sum = 0
        
        # Iterate through the dictionary and add the unique elements to the sum
        for num, freq in frequency.items():
            if freq == 1:  # If the frequency is 1, the element is unique
                unique_sum += num
        
        return unique_sum
