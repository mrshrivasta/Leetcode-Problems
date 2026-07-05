class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        n = len(seats)
        last_occupied = -1
        max_dist = 0
        
        for i in range(n):
            if seats[i] == 1:
                if last_occupied == -1:
                    # Case 1: Empty seats at the beginning of the row
                    max_dist = i
                else:
                    # Case 3: Empty seats between two occupied seats
                    max_dist = max(max_dist, (i - last_occupied) // 2)
                
                # Update the last seen occupied seat pointer
                last_occupied = i
                
        # Case 2: Empty seats at the very end of the row
        max_dist = max(max_dist, n - 1 - last_occupied)
        
        return max_dist