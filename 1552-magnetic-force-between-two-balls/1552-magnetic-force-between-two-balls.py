class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def is_feasible(d):
            # Place the first ball in the first basket
            count = 1
            last_position = position[0]
            for i in range(1, len(position)):
                if position[i] - last_position >= d:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False
        
        position.sort()
        left, right = 1, position[-1] - position[0]
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if is_feasible(mid):
                result = mid  # mid is a feasible solution
                left = mid + 1  # try for a bigger minimum distance
            else:
                right = mid - 1  # try for a smaller minimum distance
        
        return result
