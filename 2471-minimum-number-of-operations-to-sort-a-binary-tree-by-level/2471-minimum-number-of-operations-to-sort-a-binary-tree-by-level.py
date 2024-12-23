from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Perform BFS to collect values at each level
        levels = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            level_values = []
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level_values)

        # Helper function to calculate minimum swaps to sort an array
        def min_swaps_to_sort(arr: List[int]) -> int:
            n = len(arr)
            sorted_arr = sorted(arr)
            index_map = {v: i for i, v in enumerate(sorted_arr)}
            visited = [False] * n
            swaps = 0

            for i in range(n):
                if visited[i] or arr[i] == sorted_arr[i]:
                    continue

                # Count the size of the cycle
                cycle_size = 0
                x = i
                while not visited[x]:
                    visited[x] = True
                    x = index_map[arr[x]]
                    cycle_size += 1

                if cycle_size > 1:
                    swaps += cycle_size - 1

            return swaps

        # Calculate the total minimum operations across all levels
        min_operations = 0
        for level in levels:
            min_operations += min_swaps_to_sort(level)

        return min_operations
