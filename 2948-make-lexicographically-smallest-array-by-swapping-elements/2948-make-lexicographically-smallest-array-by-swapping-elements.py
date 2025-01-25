class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        
        # Union-Find (DSU) helpers
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_y] = root_x
        
        # Sort indices based on nums values
        indexed_nums = sorted((val, idx) for idx, val in enumerate(nums))
        
        # Build connections using sorted indices
        for i in range(n - 1):
            if abs(indexed_nums[i][0] - indexed_nums[i + 1][0]) <= limit:
                union(indexed_nums[i][1], indexed_nums[i + 1][1])
        
        # Group indices by their connected component
        groups = {}
        for i in range(n):
            root = find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(i)
        
        # Sort values within each connected component
        result = nums[:]
        for indices in groups.values():
            values = sorted(nums[i] for i in indices)
            for idx, val in zip(sorted(indices), values):
                result[idx] = val
        
        return result
