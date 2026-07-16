class NeighborSum:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.pos = {grid[i][j]: (i,j) for i in range(len(grid)) for j in range(len(grid[0]))}

    def adjacentSum(self, value: int) -> int:
        r, c, n, g = *self.pos[value], len(self.grid), self.grid
        return sum(g[r+dr][c+dc] for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)] if 0<=r+dr<n and 0<=c+dc<n)

    def diagonalSum(self, value: int) -> int:
        r, c, n, g = *self.pos[value], len(self.grid), self.grid
        return sum(g[r+dr][c+dc] for dr,dc in [(-1,-1),(-1,1),(1,-1),(1,1)] if 0<=r+dr<n and 0<=c+dc<n)