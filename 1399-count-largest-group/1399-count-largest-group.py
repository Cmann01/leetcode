class Solution:
    def countLargestGroup(self, n: int) -> int:
        from collections import defaultdict
        
        # Dictionary to keep count of group sizes based on digit sum
        group_count = defaultdict(int)
        
        # Calculate digit sum for each number and update group count
        for i in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(i))
            group_count[digit_sum] += 1
        
        # Find the maximum size of any group
        max_size = max(group_count.values())
        
        # Count how many groups have the maximum size
        return sum(1 for count in group_count.values() if count == max_size)
