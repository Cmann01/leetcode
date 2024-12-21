from typing import List
from collections import defaultdict

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # Build the adjacency list for the tree
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # Initialize the number of valid components
        components = 0
        
        def dfs(node, parent):
            nonlocal components
            # Compute the total sum of the subtree rooted at this node
            subtree_sum = values[node]
            
            for neighbor in tree[node]:
                if neighbor != parent:
                    child_sum = dfs(neighbor, node)
                    # Check if the child's sum is divisible by k
                    if child_sum % k == 0:
                        components += 1  # Valid component formed by cutting the edge
                    else:
                        subtree_sum += child_sum  # Add the remainder to the current node
            
            return subtree_sum
        
        # Start DFS from node 0 (or any node, since it's a tree)
        total_sum = dfs(0, -1)
        
        # If the total sum is divisible by k, the entire tree is one valid component
        if total_sum % k == 0:
            components += 1
        
        return components
