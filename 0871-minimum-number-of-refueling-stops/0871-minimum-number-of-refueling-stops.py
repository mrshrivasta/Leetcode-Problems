import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        # Max-heap to store the fuel capacities of stations we have passed
        max_heap = []
        
        stops = 0
        current_fuel = startFuel
        prev_position = 0
        
        # Append the target destination as a dummy station with 0 fuel
        # This simplifies the loop logic to handle the final stretch
        stations.append([target, 0])
        
        for position, fuel in stations:
            # Calculate the distance from the last checkpoint to the current station
            distance = position - prev_position
            
            # Consume the fuel needed to travel this distance
            current_fuel -= distance
            
            # If our fuel becomes negative, we need to retroactively refuel 
            # from the best stations we passed along the way
            while max_heap and current_fuel < 0:
                # Pop the station with the maximum fuel (invert back to positive)
                current_fuel += -heapq.heappop(max_heap)
                stops += 1
                
            # If we've refueled from all available past stations and still can't 
            # bridge the gap, it's impossible to proceed.
            if current_fuel < 0:
                return -1
                
            # We successfully reached this station. Add its fuel to our options.
            heapq.heappush(max_heap, -fuel)
            
            # Update our current position position
            prev_position = position
            
        return stops