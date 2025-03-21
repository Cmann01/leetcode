from collections import deque
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = {}  # adjacency list
        in_degree = {}  # number of ingredients needed
        
        # Initialize graph and in-degree for recipes
        for recipe in recipes:
            graph[recipe] = []
            in_degree[recipe] = 0

        # Build the dependency graph
        ingredient_to_recipe = {}
        for i, recipe in enumerate(recipes):
            for ing in ingredients[i]:
                if ing not in ingredient_to_recipe:
                    ingredient_to_recipe[ing] = []
                ingredient_to_recipe[ing].append(recipe)
                in_degree[recipe] += 1  # Increase in-degree since recipe depends on this ingredient
        
        # Initialize queue with available supplies
        queue = deque(supplies)
        possible_recipes = set(supplies)  # Ingredients available from the start
        
        result = []
        
        # Process the queue
        while queue:
            item = queue.popleft()
            
            # If it's a recipe, add to result
            if item in in_degree:
                result.append(item)
            
            # Reduce the in-degree of dependent recipes
            if item in ingredient_to_recipe:
                for recipe in ingredient_to_recipe[item]:
                    in_degree[recipe] -= 1
                    if in_degree[recipe] == 0:  # If all ingredients are available, add recipe to queue
                        queue.append(recipe)
        
        return result
