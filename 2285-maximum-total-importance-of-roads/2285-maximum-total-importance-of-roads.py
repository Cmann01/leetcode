class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Count the degree of each city
        degree = [0] * n
        for road in roads:
            degree[road[0]] += 1
            degree[road[1]] += 1
        
        # Step 2: Sort cities by their degrees in descending order
        sorted_cities = sorted(range(n), key=lambda x: degree[x], reverse=True)
        
        # Step 3: Assign values to cities
        value_assignment = [0] * n
        for i, city in enumerate(sorted_cities):
            value_assignment[city] = n - i
        
        # Step 4: Calculate the total importance of all roads
        total_importance = 0
        for road in roads:
            total_importance += value_assignment[road[0]] + value_assignment[road[1]]
        
        return total_importance
