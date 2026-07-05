class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Step 1: Ensure the most significant bit (MSB) of every row is 1
        # If the first element of a row is 0, we flip that entire row.
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1
        
        # The first column will now contribute a 1 for every row.
        # Its value contribution is m * (2^(n-1))
        score = m * (1 << (n - 1))
        
        # Step 2: For every remaining column, check if flipping it maximizes the 1s
        for j in range(1, n):
            # Count how many 1s are in the current column
            ones_count = sum(grid[i][j] for i in range(m))
            
            # We want the maximum number of 1s possible in this column,
            # which is either the current count of 1s or the count after flipping (m - ones_count)
            max_ones = max(ones_count, m - ones_count)
            
            # Add the contribution of this column to the total score
            score += max_ones * (1 << (n - 1 - j))
            
        return score