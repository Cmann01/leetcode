class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # Combine robots' data and sort by position
        robots = sorted(zip(positions, healths, directions), key=lambda x: x[0])
        
        stack = []  # Stack to hold robots moving to the right
        result = []  # List to collect surviving robots' healths

        for pos, health, dir in robots:
            if dir == 'R':
                stack.append((pos, health, dir))
            else:
                while stack and stack[-1][2] == 'R':
                    r_pos, r_health, r_dir = stack.pop()
                    if r_health > health:
                        stack.append((r_pos, r_health - 1, r_dir))
                        break
                    elif r_health < health:
                        health -= 1
                    else:
                        break
                else:
                    result.append((pos, health, dir))
        
        # Append the remaining robots in the stack to the result
        result.extend(stack)
        
        # Extract healths in the original order of input positions
        original_order = {pos: idx for idx, pos in enumerate(positions)}
        result = sorted(result, key=lambda x: original_order[x[0]])
        
        return [health for _, health, _ in result]

# Example usage:
solution = Solution()
print(solution.survivedRobotsHealths([5,4,3,2,1], [2,17,9,15,10], "RRRRR"))  # Output: [2, 17, 9, 15, 10]
print(solution.survivedRobotsHealths([3,5,2,6], [10,10,15,12], "RLRL"))  # Output: [14]
print(solution.survivedRobotsHealths([1,2,5,6], [10,10,11,11], "RLRL"))  # Output: []
