class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index_map = {value: idx for idx, value in enumerate(list1)}
        min_sum = float('inf')
        result = []

        for idx2, value in enumerate(list2):
            if value in index_map:
                idx_sum = idx2 + index_map[value]
                if idx_sum < min_sum:
                    min_sum = idx_sum
                    result = [value]
                elif idx_sum == min_sum:
                    result.append(value)
        
        return result

# Example usage:
solution = Solution()

# Example 1
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
print(solution.findRestaurant(list1, list2))  # Output: ["Shogun"]

# Example 2
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]
print(solution.findRestaurant(list1, list2))  # Output: ["Shogun"]

# Example 3
list1 = ["happy", "sad", "good"]
list2 = ["sad", "happy", "good"]
print(solution.findRestaurant(list1, list2))  # Output: ["sad", "happy"]
