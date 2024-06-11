class Solution:
    def relativeSortArray(self, arr1, arr2):
        # Create a dictionary to store the index of each element in arr2
        order_map = {val: idx for idx, val in enumerate(arr2)}
        
        # Define a custom sort key function
        def sort_key(x):
            # If x is in arr2, return its index, else return a large number and x itself for natural sorting
            return (order_map.get(x, len(arr2)), x)
        
        # Sort arr1 with the custom sort key
        arr1.sort(key=sort_key)
        
        return arr1

# Example usage:
solution = Solution()
print(solution.relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))  # Output: [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
print(solution.relativeSortArray([28, 6, 22, 8, 44, 17], [22, 28, 8, 6]))  # Output: [22, 28, 8, 6, 17, 44]
