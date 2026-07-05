class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        # Define directions clockwise: 0: North, 1: East, 2: South, 3: West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0  # Start facing North
        
        # Current coordinates of the robot
        x, y = 0, 0
        
        # Convert obstacles list into a set of tuples for O(1) lookups
        obstacle_set = {tuple(obs) for obs in obstacles}
        
        max_dist_sq = 0
        
        for cmd in commands:
            if cmd == -1:
                # Turn right 90 degrees
                d = (d + 1) % 4
            elif cmd == -2:
                # Turn left 90 degrees
                d = (d - 1) % 4
            else:
                # Move forward cmd units, one unit at a time
                dx, dy = directions[d]
                for _ in range(cmd):
                    next_x = x + dx
                    next_y = y + dy
                    
                    # If an obstacle is right in front of us, stop moving forward
                    if (next_x, next_y) in obstacle_set:
                        break
                    
                    # Update coordinates
                    x, y = next_x, next_y
                    
                # Track the maximum squared Euclidean distance reached at any point
                max_dist_sq = max(max_dist_sq, x * x + y * y)
                
        return max_dist_sq