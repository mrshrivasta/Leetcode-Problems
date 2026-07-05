import bisect

class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        # Step 1: Sort the heaters to enable binary search
        heaters.sort()
        min_radius = 0
        
        # Step 2: Find the closest heater for each house
        for house in houses:
            # Locate the insertion point for the current house
            idx = bisect.bisect_left(heaters, house)
            
            # Distance to the heater on the right (if it exists)
            dist_right = heaters[idx] - house if idx < len(heaters) else float('inf')
            
            # Distance to the heater on the left (if it exists)
            dist_left = house - heaters[idx - 1] if idx > 0 else float('inf')
            
            # The closest heater for this specific house
            closest_heater_dist = min(dist_left, dist_right)
            
            # The global radius must be large enough to cover the worst-case house
            min_radius = max(min_radius, closest_heater_dist)
            
        return min_radius