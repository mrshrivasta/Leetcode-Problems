class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Pair each car's position with its speed and sort by position in descending order
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        current_fleet_time = 0.0
        
        for pos, spd in cars:
            # Calculate the time required for the current car to reach the target independently
            time_to_target = (target - pos) / spd
            
            # If this car takes more time than the fleet ahead of it,
            # it cannot catch up. It forms a new fleet bottleneck.
            if time_to_target > current_fleet_time:
                fleets += 1
                current_fleet_time = time_to_target
                
        return fleets