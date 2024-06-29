class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict, deque
        
        # Step 1: Create the adjacency list for the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        
        # Step 2: Prepare a list to store the ancestors
        ancestors = [set() for _ in range(n)]
        
        # Step 3: Function to perform DFS and find all ancestors
        def dfs(node, ancestor):
            for neighbor in graph[node]:
                if ancestor not in ancestors[neighbor]:
                    ancestors[neighbor].add(ancestor)
                    dfs(neighbor, ancestor)
        
        # Step 4: Perform DFS from each node
        for i in range(n):
            dfs(i, i)
        
        # Step 5: Convert sets to sorted lists
        result = [sorted(list(ancestor_set)) for ancestor_set in ancestors]
        
        return result

# Example usage
sol = Solution()
n = 8
edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
print(sol.getAncestors(n, edges))  # Expected Output: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
