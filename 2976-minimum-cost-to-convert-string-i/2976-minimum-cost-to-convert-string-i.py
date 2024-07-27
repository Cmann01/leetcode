class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        import sys
        from collections import defaultdict
        
        # Initialize graph with high costs (infinity)
        inf = sys.maxsize
        graph = defaultdict(lambda: defaultdict(lambda: inf))
        
        # Populate the graph with given transformations
        for o, c, co in zip(original, changed, cost):
            graph[o][c] = min(graph[o][c], co)
        
        # Characters set
        chars = set(chr(ord('a') + i) for i in range(26))
        
        # Floyd-Warshall algorithm to find shortest path between all pairs of nodes
        for k in chars:
            for i in chars:
                for j in chars:
                    if graph[i][j] > graph[i][k] + graph[k][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]
        
        # Calculate the minimum cost to transform source to target
        total_cost = 0
        for s_char, t_char in zip(source, target):
            if s_char == t_char:
                continue
            min_cost = graph[s_char][t_char]
            if min_cost == inf:
                return -1
            total_cost += min_cost
        
        return total_cost

# Example usage:
solution = Solution()
source = "abcd"
target = "acbe"
original = ["a", "b", "c", "c", "e", "d"]
changed = ["b", "c", "b", "e", "b", "e"]
cost = [2, 5, 5, 1, 2, 20]
print(solution.minimumCost(source, target, original, changed, cost))  # Output: 28
