class Solution:
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        flat = [grid[i][j] for i in range(m) for j in range(n)]
        k %= len(flat)
        flat = flat[-k:] + flat[:-k]
        return [flat[i*n:(i+1)*n] for i in range(m)]