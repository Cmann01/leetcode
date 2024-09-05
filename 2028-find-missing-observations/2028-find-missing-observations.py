class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # Step 1: Calculate the total sum that should be achieved
        m = len(rolls)
        total_sum = mean * (n + m)
        
        # Step 2: Calculate the known sum from the given rolls
        known_sum = sum(rolls)
        
        # Step 3: Calculate the missing sum that needs to be distributed across n rolls
        missing_sum = total_sum - known_sum
        
        # Step 4: Check if it's possible to achieve missing_sum with n rolls
        if missing_sum < n * 1 or missing_sum > n * 6:
            return []
        
        # Step 5: Distribute the missing_sum across n rolls
        result = [1] * n  # Start by giving each roll the minimum value of 1
        missing_sum -= n  # We've already assigned n * 1
        
        # Distribute the remaining sum across the rolls
        for i in range(n):
            add_value = min(5, missing_sum)  # Add at most 5 to each roll
            result[i] += add_value
            missing_sum -= add_value
            if missing_sum == 0:
                break
        
        return result
