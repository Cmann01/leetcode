import heapq

class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        # Create a list of projects (capital, profit)
        projects = list(zip(capital, profits))
        
        # Min-heap based on the required capital to start the project
        min_capital_heap = []
        for c, p in projects:
            heapq.heappush(min_capital_heap, (c, p))
        
        # Max-heap based on the profit of the projects
        max_profit_heap = []
        
        current_capital = w
        
        for _ in range(k):
            # Move all feasible projects to the max-heap
            while min_capital_heap and min_capital_heap[0][0] <= current_capital:
                c, p = heapq.heappop(min_capital_heap)
                heapq.heappush(max_profit_heap, (-p, c))
            
            # If no projects are feasible, break
            if not max_profit_heap:
                break
            
            # Select the most profitable project
            current_capital += -heapq.heappop(max_profit_heap)[0]
        
        return current_capital

# Example usage
sol = Solution()
print(sol.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))  # Output: 4
print(sol.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]))  # Output: 6
