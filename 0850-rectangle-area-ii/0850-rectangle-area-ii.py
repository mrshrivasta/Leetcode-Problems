class Solution:
    def rectangleArea(self, rectangles: list[list[int]]) -> int:
        MOD = 10**9 + 7
        
        # Events will store tuples of (x_coordinate, type, y1, y2)
        # type: 1 for entering a rectangle, -1 for leaving a rectangle
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, 1, y1, y2))
            events.append((x2, -1, y1, y2))
            
        # Sort events primarily by x-coordinate
        events.sort(key=lambda e: e[0])
        
        # Tracks active y-intervals currently intersected by the sweep-line
        active_y_intervals = []
        
        def calculate_total_y(intervals):
            """Helper function to merge overlapping intervals and calculate total length"""
            if not intervals:
                return 0
            # Sort intervals by their starting y-coordinate
            intervals.sort(key=lambda inv: inv[0])
            
            total_y = 0
            curr_y1, curr_y2 = intervals[0]
            
            for y1, y2 in intervals[1:]:
                if y1 < curr_y2:
                    # Overlap found, extend the current interval
                    curr_y2 = max(curr_y2, y2)
                else:
                    # No overlap, add previous interval length and start a new one
                    total_y += curr_y2 - curr_y1
                    curr_y1, curr_y2 = y1, y2
                    
            total_y += curr_y2 - curr_y1
            return total_y

        total_area = 0
        prev_x = events[0][0]
        
        for x, type_val, y1, y2 in events:
            # Calculate width change
            delta_x = x - prev_x
            
            if delta_x > 0:
                # Calculate active vertical length and add area interval
                total_area += delta_x * calculate_total_y(active_y_intervals)
                total_area %= MOD
            
            # Update the active y-intervals
            if type_val == 1:
                active_y_intervals.append((y1, y2))
            else:
                active_y_intervals.remove((y1, y2))
                
            prev_x = x
            
        return total_area