from typing import List
from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total_boomerangs = 0
        
        for x1, y1 in points:
            # Hash map to store: { squared_distance: frequency }
            distance_map = defaultdict(int)
            
            for x2, y2 in points:
                # Calculate squared Euclidean distance
                dx = x1 - x2
                dy = y1 - y2
                squared_dist = dx * dx + dy * dy
                
                distance_map[squared_dist] += 1
            
            # Calculate permutations for each distance group
            for count in distance_map.values():
                if count > 1:
                    total_boomerangs += count * (count - 1)
                    
        return total_boomerangs