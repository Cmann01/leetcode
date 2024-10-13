import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Min-heap to store the current element of each list
        min_heap = []
        max_value = float('-inf')
        
        # Initialize the heap with the first element from each list
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            max_value = max(max_value, nums[i][0])
        
        # Initialize the smallest range
        start, end = float('-inf'), float('inf')
        
        # Process the heap
        while min_heap:
            min_value, list_index, element_index = heapq.heappop(min_heap)
            
            # Update the smallest range if necessary
            if max_value - min_value < end - start:
                start, end = min_value, max_value
            
            # If we've exhausted one of the lists, we can't proceed
            if element_index + 1 == len(nums[list_index]):
                break
            
            # Get the next element from the list and push it to the heap
            next_element = nums[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_element, list_index, element_index + 1))
            
            # Update the maximum value
            max_value = max(max_value, next_element)
        
        return [start, end]
