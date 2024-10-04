from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Step 1: Sort the skills array
        skill.sort()
        
        # Step 2: Set the target team skill sum
        target = skill[0] + skill[-1]
        
        # Initialize the sum of chemistry
        total_chemistry = 0
        
        # Step 3: Try to form valid teams
        i, j = 0, len(skill) - 1
        while i < j:
            if skill[i] + skill[j] != target:
                return -1  # If the sum of skills doesn't match the target, return -1
            # Step 4: Calculate chemistry and accumulate the result
            total_chemistry += skill[i] * skill[j]
            i += 1
            j -= 1
        
        # Step 5: Return the total chemistry of all teams
        return total_chemistry
