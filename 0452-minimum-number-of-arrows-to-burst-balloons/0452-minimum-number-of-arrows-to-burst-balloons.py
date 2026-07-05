class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # Sort the balloons based on their end coordinates
        points.sort(key=lambda x: x[1])
        
        # Initialize the first arrow at the end of the first balloon
        arrows = 1
        current_end = points[0][1]
        
        # Iterate through the rest of the balloons
        for i in range(1, len(points)):
            # If the current balloon starts after the last arrow position,
            # we need a new arrow.
            if points[i][0] > current_end:
                arrows += 1
                current_end = points[i][1]  # Update arrow position to this balloon's end
                
        return arrows