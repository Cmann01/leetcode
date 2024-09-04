class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Directions are in the order: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_direction = 0  # Start facing north
        x, y = 0, 0  # Starting position
        max_distance = 0
        
        # Convert the list of obstacles to a set of tuples for O(1) lookup
        obstacle_set = set(map(tuple, obstacles))
        
        for command in commands:
            if command == -1:  # Turn right 90 degrees
                current_direction = (current_direction + 1) % 4
            elif command == -2:  # Turn left 90 degrees
                current_direction = (current_direction - 1) % 4
            else:  # Move forward command units
                dx, dy = directions[current_direction]
                for _ in range(command):
                    # Check the next position
                    if (x + dx, y + dy) not in obstacle_set:
                        x += dx
                        y += dy
                        # Update the maximum distance
                        max_distance = max(max_distance, x*x + y*y)
                    else:
                        # Stop moving in this direction if an obstacle is encountered
                        break
        
        return max_distance
