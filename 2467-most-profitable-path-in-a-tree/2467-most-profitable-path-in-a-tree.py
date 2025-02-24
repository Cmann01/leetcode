from collections import defaultdict, deque

class Solution:
    def mostProfitablePath(self, edges, bob, amount):
        n = len(amount)
        alice_income = float('-inf')

        # Create adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # DFS to find Bob's reach time to each node
        visited = [False] * n
        bob_map = {}
        self.dfs_bob(bob, visited, adj, bob_map, 0)

        # BFS for Alice's traversal
        visited = [False] * n
        que = deque([(0, 0, 0)])  # (current_node, time, income)

        while que:
            curr, time, income = que.popleft()

            if curr not in bob_map or bob_map[curr] > time:
                income += amount[curr]
            elif time == bob_map[curr]:
                income += amount[curr] // 2  # Bob and Alice reach at the same time

            # If it's a leaf node (except node 0)
            if len(adj[curr]) == 1 and curr != 0:
                alice_income = max(alice_income, income)

            visited[curr] = True  # Mark as visited

            for ngbr in adj[curr]:
                if not visited[ngbr]:
                    que.append((ngbr, time + 1, income))

        return alice_income

    def dfs_bob(self, curr, visited, adj, bob_map, t):
        visited[curr] = True
        bob_map[curr] = t

        if curr == 0:
            return True

        for ngbr in adj[curr]:
            if not visited[ngbr]:
                if self.dfs_bob(ngbr, visited, adj, bob_map, t + 1):
                    return True

        bob_map.pop(curr, None)
        return False
