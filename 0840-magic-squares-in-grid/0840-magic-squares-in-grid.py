class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if rows < 3 or cols < 3:
            return 0
        
        def isMagic(r, c):
            # 1. The center element must be 5
            if grid[r+1][c+1] != 5:
                return False
            
            # 2. Check if it contains unique numbers from 1 to 9
            vals = [
                grid[r][c],   grid[r][c+1],   grid[r][c+2],
                grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]
            ]
            if sorted(vals) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False
            
            # 3. Check row sums (already verified implicitly by checking diagonals/cols, 
            # but explicit checks are fast and clean)
            if (grid[r][c] + grid[r][c+1] + grid[r][c+2] != 15 or
                grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] != 15 or
                grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] != 15):
                return False
                
            # 4. Check column sums
            if (grid[r][c] + grid[r+1][c] + grid[r+2][c] != 15 or
                grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] != 15 or
                grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != 15):
                return False
                
            # 5. Check diagonal sums
            if (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 or
                grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c+1] != 15): # wait, main diag and anti-diag
                pass 
                
            # Correcting anti-diagonal check layout
            if (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 or
                grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15):
                return False
                
            return True

        magic_squares_count = 0
        
        # Slide the 3x3 window over the entire grid
        for r in range(rows - 2):
            for c in range(cols - 2):
                if isMagic(r, c):
                    magic_squares_count += 1
                    
        return magic_squares_count