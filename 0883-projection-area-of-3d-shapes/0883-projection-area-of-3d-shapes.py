class Solution:
    def projectionArea(self, grid):
        n = len(grid)
        xy = sum(1 for i in range(n) for j in range(n) if grid[i][j])
        yz = sum(max(grid[i][j] for i in range(n)) for j in range(n))
        zx = sum(max(grid[i][j] for j in range(n)) for i in range(n))
        return xy + yz + zx